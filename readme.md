# Python's Abstract Syntax Tree: Practical and Unpractical Uses

Slides and some code for my PyCon Austria 2025 talk.

## Objective

My goal was to demystify the concept of abstract syntax trees (AST).  
The name is a bit scary, and it often comes up in conversations on topics (compilers, interpreters) that might not be familiar to all software engineers.

But it's not that hard to get started and benefit from the magic of AST manipulation.

## Code

The code in `assert_transformer.py` shows the code presented in the slides as a 'proof of concept' of a transform to achieve a pytest-like experience.  
It is a bit simplistic - to fit on slides and focus the discussion - but the principle is there.

Tested with Python 3.11. 

## References

On pytest using AST transforms:

- [pytest blog post](http://pybites.blogspot.be/2011/07/behind-scenes-of-pytests-new-assertion.html)
- A relevant part of [pytest source code](https://github.com/pytest-dev/pytest/blob/be83aa618c68ebb9080b537bbd8b19b97a7f4eb8/src/_pytest/assertion/rewrite.py#L615">https://github.com/pytest-dev/pytest/blob/be83aa618c68ebb9080b537bbd8b19b97a7f4eb8/src/_pytest/assertion/rewrite.py#L615)

General resources:

- [Unofficial AST docs](https://greentreesnakes.readthedocs.io/en/latest/)
- [https://eli.thegreenplace.net/2009/11/28/python-internals-working-with-python-asts](https://eli.thegreenplace.net/2009/11/28/python-internals-working-with-python-asts)
This is a fantastic blog, and these 'old' blog posts are still relevant.
- My talk was not recorded, if you want a video I enjoyed "The AST and Me": [video](https://www.youtube.com/watch?v=XhWvz4dK4ng), [slides](https://emilyemorehouse.github.io/ast-and-me/).

- Someone asked about macros in Python at the end of the talk. There are multiple projects, the most popular one seems to be: [https://github.com/lihaoyi/macropy](https://github.com/lihaoyi/macropy).
[The docs](https://macropy3.readthedocs.io/en/latest/overview.html) give a good primer on the 'behind the scenes'. I see two main components: AST transforms and import hooks to modify the way modules are loaded (basically apply the transforms and return the new module).



## Abstract

Peek under the hood of Python and unlock the power of its Abstract Syntax Tree! We’ll demystify the AST, explore how it powers tools like pytest, linters, and refactoring, and experiment with more… creative transformations.

What is the Python Abstract Syntax Tree and why should you care? In this talk, we’ll demystify the Abstract Syntax Tree (AST) and show how it powers tools you probably already use - in Python and other languages.

We’ll take a close look at pytest assert rewrite as a motivating and empowering example of how AST transformations work.

ASTs (and their cousins, the Concrete Syntax Trees) drive many real-world applications, from linters to automatic refactoring. We’ll mention some modern tools you might want to use.

Armed with newfound confidence, we’ll explore more creative transformations.

You’ll leave this talk with a deeper understanding of Python’s internals and a few terrible ideas for AST-powered tools.

This talk is beginner-friendly, no prior AST knowledge required.

