from FSMSIM.expr.arr_expr import ArrayExpr
from FSMSIM.expr.expr import Expr

class ArrayAccessExpr(Expr):
    def __init__(self, arr: "ArrayExpr", field: str) -> None:
        self.arr = arr
        self.field = field
    
    def evaluate(self) -> str:
        return self.arr.evaluate(self.field)
    
    def __len__(self) -> int:
        return self.arr.len(self.field)
    
    def fieldlen(self) -> int:
        return self.arr.fieldlen(self.field)
