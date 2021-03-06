from FSMSIM.expr.expr import Expr

class StringExpr(Expr):
    def __init__(self, s: str) -> None:
        self.val = s
    
    def evaluate(self) -> str:
        return self.val

    def __len__(self) -> int:
        return len(self.val)
