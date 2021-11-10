from FSMSIM.expr.output_expr import OutputExpr
from FSMSIM.state import State
from FSMSIM.expr.expr import Expr
from FSMSIM.expr.var_expr import VarExpr
from collections.abc import Iterable
import copy

def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

class Module:
    def __init__(self) -> None:
        self.inputs = dict()
        self.outputs = dict()
        self.children = dict()
        self.states = dict()
        self.default_state = State()
        self.states["_"] = self.default_state
        self.curr_state = "_"
        self.next_state = None
        self.clock_cycles = 1

    def init(self) -> "Module":
        return copy.deepcopy(self)
    
    def define_input(self, name: str, length: int = 1, value: Expr = None):
        self.inputs[name] = VarExpr(length) if value is None else value
    
    def define_output(self, name: str, length: int = 1, value: Expr = None):
        self.default_state.define_output(name, VarExpr(length) if value is None else value)
        self.outputs[name] = OutputExpr(self, name)
    
    def define_state(self, name: str):
        self.states[name] = State(self.default_state)
    
    def define_initial_state(self, name: str):
        self.curr_state = name
    
    def define_clock_cycles(self, count: int):
        self.clock_cycles = count
    
    def get_output(self, name: str) -> Expr:
        return self.states[self.curr_state].get_output(name)
    
    def evaluate(self):
        for _ in range(self.clock_cycles):
            for child in flatten(self.children.values()):
                child.evaluate()
            for child in flatten(self.children.values()):
                child.tick()
        self.next_state = self.states[self.curr_state].transit()
        if self.next_state is None:
            self.next_state = self.curr_state
    
    def tick(self):
        if self.next_state is None:
            self.evaluate()
        self.curr_state = self.next_state
        self.next_state = None
