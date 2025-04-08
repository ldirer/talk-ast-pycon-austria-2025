import ast


class RewriteAssertNodeTransformer(ast.NodeTransformer):
    def visit_Assert(self, node):
        transformer = AddIntermediateVariablesTransformer()
        node = transformer.visit(node)
        assignments = list(reversed(transformer.assignments))

        except_handler = ast.ExceptHandler(
            type=ast.Name(id="AssertionError", ctx=ast.Load()),
            name="e",
            body=[*get_print_nodes(assignments), ast.Raise()],
        )

        return ast.Try(
            body=[*assignments, node],
            handlers=[except_handler],
            orelse=[],
            finalbody=[],
        )


def get_print_nodes(assignments: list[ast.Assign]) -> list[ast.Expr]:
    nodes = []
    for assignment in assignments:
        variable_id = assignment.targets[0].id
        print_args = [
            ast.Constant(f"{variable_id}="),
            ast.Name(id=variable_id, ctx=ast.Load()),
        ]
        nodes.append(
            ast.Expr(
                ast.Call(ast.Name(id="print", ctx=ast.Load()), print_args, [])
            )
        )

    return nodes


def get_friendly_variable_name(node):
    return ast.unparse(node)


class AddIntermediateVariablesTransformer(ast.NodeTransformer):
    variable_prefix = "intermediate_"

    def __init__(self):
        super().__init__()
        # A list of the assignment nodes we need for our transformed node to make sense
        # We will insert these before the transformed node so all variables we refer to are defined.
        self.assignments = []
        self.variable_counter = 1

    def visit_Call(self, node):
        return self.collect_assignments_and_transform(node)

    def visit_BinOp(self, node):
        return self.collect_assignments_and_transform(node)

    def collect_assignments_and_transform(self, node):
        variable_id = self.get_variable_id(node)
        self.assignments.append(
            ast.Assign(
                targets=[ast.Name(id=variable_id, ctx=ast.Store())], value=node
            )
        )
        self.variable_counter += 1
        self.generic_visit(node)
        return ast.copy_location(
            ast.Name(id=variable_id, ctx=ast.Load()), node
        )

    def get_variable_id(self, node):
        name = get_friendly_variable_name(node)
        variable_id = f"{self.variable_prefix}{self.variable_counter}_{name}"
        return variable_id


if __name__ == '__main__':
    # show the 'transformed code' for a simple example
    # note that the transformed code is... not valid python code!
    # Python could not parse it back
    # Python can execute it just fine in AST form (before 'ast.unparse'), see commented code below
    source = "assert square(add(a, b)) == expected - 1"

    node = ast.parse(source)
    transformed = RewriteAssertNodeTransformer().visit(node)
    transformed = ast.fix_missing_locations(transformed)

    # uncomment below to run the transformed code.
    # this should fail with an AssertionError, printing values of intermediate variables.
    # compiled = compile(transformed, "<ast>", "exec")
    # # we need to provide values for the variables referenced in the statement
    # exec(compiled, {"add": lambda x, y: x + y, "square": lambda x: x ** 2, "a": 1, "b": 2, "expected": 9, })

    print(ast.unparse(transformed))
