from FSMSIM.expr.expr import Expr

class SliceExpr(Expr):
    def __init__(self, val: Expr, start=0, end=-1) -> None:
        self.val = val
        self.start = start
        self.end = end
    
    def evaluate(self) -> str:
        return self.val.evaluate()[self.start:self.end]