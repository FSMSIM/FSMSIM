class BoolExpr:
    def __init__(self, val: bool) -> None:
        self.val = val
        
    def evaluate(self) -> bool:
        return self.val
