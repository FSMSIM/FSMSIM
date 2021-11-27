from FSMSIM.expr.expr import Expr

class OutputExpr(Expr):
    def __init__(self, mod, name: str, length: int) -> None:
        self.mod = mod
        self.name = name
        self.l = length
    
    def evaluate(self) -> str:
        return self.mod.get_output(self.name).evaluate()
    
    def __len__(self) -> int:
        return self.l