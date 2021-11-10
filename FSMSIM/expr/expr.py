class Expr:
    def evaluate(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.evaluate()

    def __repr__(self) -> str:
        return self.evaluate()