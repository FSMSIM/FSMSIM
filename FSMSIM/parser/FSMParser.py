# Generated from /Users/haoyuanliu/Developer/cs263/proj/FSMSIM/parser/FSMParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\t\4\2\t\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\7\2\4\3\2")
        buf.write("\2\2\4\5\7\6\2\2\5\6\7\b\2\2\6\7\7\3\2\2\7\3\3\2\2\2\2")
        return buf.getvalue()


class FSMParser ( Parser ):

    grammarFileName = "FSMParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'import'" ]

    symbolicNames = [ "<INVALID>", "SEMICOLON", "LEFTBRACKET", "RIGHTBRACKET", 
                      "IMPORT", "INT", "STRING", "ID", "NEWLINE", "WS", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_importStmt = 0

    ruleNames =  [ "importStmt" ]

    EOF = Token.EOF
    SEMICOLON=1
    LEFTBRACKET=2
    RIGHTBRACKET=3
    IMPORT=4
    INT=5
    STRING=6
    ID=7
    NEWLINE=8
    WS=9
    COMMENT=10
    LINE_COMMENT=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ImportStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(FSMParser.IMPORT, 0)

        def STRING(self):
            return self.getToken(FSMParser.STRING, 0)

        def SEMICOLON(self):
            return self.getToken(FSMParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return FSMParser.RULE_importStmt




    def importStmt(self):

        localctx = FSMParser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(FSMParser.IMPORT)
            self.state = 3
            self.match(FSMParser.STRING)
            self.state = 4
            self.match(FSMParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





