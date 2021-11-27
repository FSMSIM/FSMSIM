from FSMSIM.expr.bool_expr import BoolExpr
from FSMSIM.expr.expr import Expr
from FSMSIM.transition import Transition
from collections import deque

class State:
    def __init__(self, defaults: "State" = None) -> None:
        self.transitions = deque()
        self.outputs = dict()
        self.defaults = defaults
        self.lengths = dict()

    def define_output(self, name: str, output: Expr):
        lengths = self.lengths if self.defaults is None else self.defaults.lengths
        assert(len(output) == lengths[name])
        self.outputs[name] = output

    def get_output(self, name: str) -> Expr:
        if name in self.outputs:
            return self.outputs[name]
        if self.defaults:
            return self.defaults.get_output(name)
        raise ValueError("Output {} not defined".format(name))

    def define_transition(self, rule: BoolExpr, target: str):
        self.transitions.appendleft(Transition(rule, target))
    
    def transit(self):
        for tr in self.transitions:
            if tr.evaluate():
                return tr.target
        if self.defaults:
            return self.defaults.transit()
