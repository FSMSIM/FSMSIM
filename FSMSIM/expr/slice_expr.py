from FSMSIM.expr.expr import Expr

class SliceExpr(Expr):
    def __init__(self, val: Expr, start=0, end=-1) -> None:
        self.val = val
        l = len(val)
        self.start = start if start >= 0 else l + start
        self.end = end if end >= 0 else l + end
        assert(0 <= self.start < l)
        assert(0 <= self.end < l)
    
    def evaluate(self) -> str:
        return self.val.evaluate()[self.start:self.end]
    
    def __len__(self) -> int:
        return self.end - self.start
