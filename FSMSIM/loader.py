import os
import re
from antlr4 import *
from FSMSIM.parser import *

FOR_PATTERN = re.compile(r"for\s*([a-zA-Z][a-zA-Z0-9_]*)\s*in\s*\[\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\]\s*{", re.S)

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
        with open(path, "r") as f:
            code = f.read()
            code = self.rewrite(code)
        input_stream = InputStream(code)
        lexer = FSMLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FSMParser(stream)
        parser.init(self)
        parser.start()
        self.loading.remove(path)
        self.loaded.add(path)

    def rewrite(self, code):
        match = FOR_PATTERN.search(code)
        while match is not None:
            var = match.group(1)
            start = int(match.group(2))
            end = int(match.group(3))
            step = int(match.group(4))
            body_start = match.end(0)
            body_end = body_start
            count = 1
            while count > 0:
                if code[body_end] == "}":
                    count -= 1
                elif code[body_end] == "{":
                    count += 1
                body_end += 1
            body = code[body_start:body_end - 1]
            body = self.rewrite(body)
            unrolled = []
            for i in range(start, end, step):
                unrolled.append("${} = {};".format(var, i))
                unrolled.append(body)
            # unrolled.append("del ${};".format(var))
            code = code[:match.start(0)] + "".join(unrolled) + code[body_end:]
            match = FOR_PATTERN.search(code)
        return code
