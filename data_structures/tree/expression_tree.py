"""ExpressionTree: Implementation of Expression Tree."""

__author__ = "{Imad Dabbura}"
from .binary_tree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left_tree=None, right_tree=None):
        super().__init__()
        if not isinstance(token, str):
            raise ValueError("Token must be a string")
        elif token not in "+-x/":
            raise ValueError("Token must be `+-x/`")
        self._add_root(token)
        if left_tree:
            self._attach(self.root(), left_tree, right_tree)

    def __str__(self):
        ans = []
        self._parethesize(self.root(), ans)
        return "".join(ans)

    def _parethesize(self, p, resutlt):
        if self.is_leaf(p):
            resutlt.append(str(p.element()))
        else:
            resutlt.append("(")
            self._parethesize(self.left(p), resutlt)
            resutlt.append(p.element())
            self._parethesize(self.right(p), resutlt)
            resutlt.append(")")

    def evaluate(self):
        return self._evaluate(self.root())

    def _evaluate(self, p):
        if self.is_leaf(p):
            return float(p.element())
        op = p.element()
        x = self._evaluate(self.left(p))
        y = self._evaluate(self.right(p))
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "/":
            return x / y
        else:
            return x * y
