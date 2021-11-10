from FSMSIM.expr.bool_expr import BoolExpr

class Transition:
    def __init__(self, rule: BoolExpr, target: str) -> None:
        self.rule = rule
        self.target = target

    def evaluate(self) -> bool:
        return self.rule.evaluate()
