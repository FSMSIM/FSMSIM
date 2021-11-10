from FSMSIM.expr.expr import Expr

class OutputExpr(Expr):
    def __init__(self, mod, name: str) -> None:
        self.mod = mod
        self.name = name
    
    def evaluate(self) -> str:
        return self.mod.get_output(self.name).evaluate()
        