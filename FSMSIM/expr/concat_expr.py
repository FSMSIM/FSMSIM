from FSMSIM.expr.expr import Expr

class ConcatExpr(Expr):
    def __init__(self, l: Expr, r: Expr) -> None:
        self.l = l
        self.r = r
    
    def evaluate(self) -> str:
        return self.l.evaluate() + self.r.evaluate()
    
    def __len__(self) -> int:
        return len(self.l) + len(self.r)
