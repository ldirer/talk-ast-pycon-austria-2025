import ast

from _pytest.assertion.rewrite import AssertionRewriter

if __name__ == "__main__":
    source = "assert square(add(a, b)) == expected - 1".encode()
    tree = ast.parse(source)

    AssertionRewriter(module_path=None, config=None, source=source).run(tree)
    unparsed = ast.unparse(tree)
    print(unparsed)
