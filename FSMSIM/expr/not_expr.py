from FSMSIM.expr.bool_expr import BoolExpr

class NotExpr(BoolExpr):
    def __init__(self, b: BoolExpr) -> None:
        self.b = b

    def evaluate(self) -> bool:
        return not self.b.evaluate()
