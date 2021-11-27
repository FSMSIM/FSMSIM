import os
from antlr4 import *
from FSMSIM.parser import *

class ModuleLoader:
    def __init__(self) -> None:
        self.modules = dict()
        self.loaded = set()
        self.loading = set()

    def register(self, name, module):
        if name in self.modules:
            raise NameError()
        self.modules[name] = module
    
    def load(self, path):
        path = os.path.abspath(path)
        if path in self.loaded:
            return
        if path in self.loading:
            raise RecursionError()
        self.loading.add(path)
        input_stream = FileStream(path)
        lexer = FSMLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FSMParser(stream)
        parser.init(self)
        parser.start()
        self.loading.remove(path)
        self.loaded.add(path)
