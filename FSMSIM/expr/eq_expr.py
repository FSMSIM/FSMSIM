from FSMSIM.expr.bool_expr import BoolExpr
from FSMSIM.expr.expr import Expr

class EqExpr(BoolExpr):
    def __init__(self, l: Expr, r: Expr) -> None:
        self.l = l
        self.r = r

    def evaluate(self) -> bool:
        return self.l.evaluate() == self.r.evaluate()
