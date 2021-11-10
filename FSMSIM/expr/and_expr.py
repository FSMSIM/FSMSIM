from FSMSIM.expr.bool_expr import BoolExpr

class AndExpr(BoolExpr):
    def __init__(self, l: BoolExpr, r: BoolExpr) -> None:
        self.l = l
        self.r = r

    def evaluate(self) -> bool:
        return self.l.evaluate() and self.r.evaluate()
