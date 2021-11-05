# Generated from /Users/haoyuanliu/Developer/cs263/proj/FSMSIM/parser/FSMLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("\u008f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\5\6\65\n\6\3\7\6\78\n\7\r\7\16\79\3\b\3\b\6\b>\n\b")
        buf.write("\r\b\16\b?\3\t\3\t\7\tD\n\t\f\t\16\tG\13\t\3\t\3\t\3\t")
        buf.write("\7\tL\n\t\f\t\16\tO\13\t\3\t\5\tR\n\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\7\r]\n\r\f\r\16\r`\13\r\3\16\3\16")
        buf.write("\3\17\6\17e\n\17\r\17\16\17f\3\17\3\17\3\20\6\20l\n\20")
        buf.write("\r\20\16\20m\3\20\3\20\3\21\3\21\3\21\3\21\7\21v\n\21")
        buf.write("\f\21\16\21y\13\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\7\22\u0084\n\22\f\22\16\22\u0087\13\22\3\22")
        buf.write("\5\22\u008a\n\22\3\22\3\22\3\22\3\22\4w\u0085\2\23\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\2\17\2\21\b\23\2\25\2\27\2\31\t\33")
        buf.write("\2\35\n\37\13!\f#\r\3\2\b\5\2\f\f\17\17$$\5\2\f\f\17\17")
        buf.write("))\3\2\62;\5\2C\\aac|\4\2\f\f\17\17\5\2\13\f\16\17\"\"")
        buf.write("\2\u0095\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\21\3\2\2\2\2\31\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'\3\2")
        buf.write("\2\2\7)\3\2\2\2\t+\3\2\2\2\13\64\3\2\2\2\r\67\3\2\2\2")
        buf.write("\17;\3\2\2\2\21Q\3\2\2\2\23S\3\2\2\2\25U\3\2\2\2\27W\3")
        buf.write("\2\2\2\31Y\3\2\2\2\33a\3\2\2\2\35d\3\2\2\2\37k\3\2\2\2")
        buf.write("!q\3\2\2\2#\177\3\2\2\2%&\7=\2\2&\4\3\2\2\2\'(\7*\2\2")
        buf.write("(\6\3\2\2\2)*\7+\2\2*\b\3\2\2\2+,\7k\2\2,-\7o\2\2-.\7")
        buf.write("r\2\2./\7q\2\2/\60\7t\2\2\60\61\7v\2\2\61\n\3\2\2\2\62")
        buf.write("\65\5\r\7\2\63\65\5\17\b\2\64\62\3\2\2\2\64\63\3\2\2\2")
        buf.write("\65\f\3\2\2\2\668\5\27\f\2\67\66\3\2\2\289\3\2\2\29\67")
        buf.write("\3\2\2\29:\3\2\2\2:\16\3\2\2\2;=\7/\2\2<>\5\27\f\2=<\3")
        buf.write("\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\20\3\2\2\2AE\7$")
        buf.write("\2\2BD\5\23\n\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2")
        buf.write("\2FH\3\2\2\2GE\3\2\2\2HR\7$\2\2IM\7)\2\2JL\5\25\13\2K")
        buf.write("J\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OM\3")
        buf.write("\2\2\2PR\7)\2\2QA\3\2\2\2QI\3\2\2\2R\22\3\2\2\2ST\n\2")
        buf.write("\2\2T\24\3\2\2\2UV\n\3\2\2V\26\3\2\2\2WX\t\4\2\2X\30\3")
        buf.write("\2\2\2Y^\5\33\16\2Z]\5\33\16\2[]\5\27\f\2\\Z\3\2\2\2\\")
        buf.write("[\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\32\3\2\2\2`")
        buf.write("^\3\2\2\2ab\t\5\2\2b\34\3\2\2\2ce\t\6\2\2dc\3\2\2\2ef")
        buf.write("\3\2\2\2fd\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\b\17\2\2i\36")
        buf.write("\3\2\2\2jl\t\7\2\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2")
        buf.write("\2\2no\3\2\2\2op\b\20\2\2p \3\2\2\2qr\7\61\2\2rs\7,\2")
        buf.write("\2sw\3\2\2\2tv\13\2\2\2ut\3\2\2\2vy\3\2\2\2wx\3\2\2\2")
        buf.write("wu\3\2\2\2xz\3\2\2\2yw\3\2\2\2z{\7,\2\2{|\7\61\2\2|}\3")
        buf.write("\2\2\2}~\b\21\2\2~\"\3\2\2\2\177\u0080\7\61\2\2\u0080")
        buf.write("\u0081\7\61\2\2\u0081\u0085\3\2\2\2\u0082\u0084\13\2\2")
        buf.write("\2\u0083\u0082\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0089\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0088\u008a\7\17\2\2\u0089\u0088\3\2\2")
        buf.write("\2\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c")
        buf.write("\7\f\2\2\u008c\u008d\3\2\2\2\u008d\u008e\b\22\2\2\u008e")
        buf.write("$\3\2\2\2\20\2\649?EMQ\\^fmw\u0085\u0089\3\b\2\2")
        return buf.getvalue()


class FSMLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SEMICOLON = 1
    LEFTBRACKET = 2
    RIGHTBRACKET = 3
    IMPORT = 4
    INT = 5
    STRING = 6
    ID = 7
    NEWLINE = 8
    WS = 9
    COMMENT = 10
    LINE_COMMENT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "')'", "'import'" ]

    symbolicNames = [ "<INVALID>",
            "SEMICOLON", "LEFTBRACKET", "RIGHTBRACKET", "IMPORT", "INT", 
            "STRING", "ID", "NEWLINE", "WS", "COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "SEMICOLON", "LEFTBRACKET", "RIGHTBRACKET", "IMPORT", 
                  "INT", "POSINT", "NEGINT", "STRING", "DoubleStringCharacter", 
                  "SingleStringCharacter", "DIGIT", "ID", "ID_LETTER", "NEWLINE", 
                  "WS", "COMMENT", "LINE_COMMENT" ]

    grammarFileName = "FSMLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


