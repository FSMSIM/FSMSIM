from FSMSIM.expr.arr_access_expr import ArrayAccessExpr
from FSMSIM.expr.expr import Expr

class SliceExpr(Expr):
    def __init__(self, val: Expr, start=0, end=-1) -> None:
        self.val = val
        l = val.fieldlen() if type(val) == ArrayAccessExpr else len(val)
        if end is None:
            end = l
        self.start = start if start >= 0 else l + start
        self.end = end if end >= 0 else l + end
        assert(self.start <= self.end)
        assert(0 <= self.start < l)
        assert(0 <= self.end <= l)
    
    def evaluate(self) -> str:
        if type(self.val) == ArrayAccessExpr:
            l = len(self.val)
            fl = self.val.fieldlen()
            return "".join([self.val.evaluate()[i+self.start:i+self.end] for i in range(0, l, fl)])
        else:
            return self.val.evaluate()[self.start:self.end]
    
    def __len__(self) -> int:
        l = self.end - self.start
        if type(self.val) == ArrayAccessExpr:
            fl = self.val.fieldlen()
            if fl > 0:
                l *= len(self.val) // fl
        return l
