from FSMSIM.expr.expr import Expr
from FSMSIM.expr.string_expr import StringExpr

class VarExpr(Expr):
    def __init__(self, l: int) -> None:
        self.l = l
        self.val = StringExpr("0" * l)
    
    def set(self, val):
        if isinstance(val, Expr):
            self.val = val
        elif isinstance(val, str):
            assert len(val) == self.l
            self.val = StringExpr(val)
    
    def evaluate(self) -> str:
        return self.val.evaluate()
    
    def __len__(self) -> int:
        return self.l
