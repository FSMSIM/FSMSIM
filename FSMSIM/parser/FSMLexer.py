# Generated from /Users/haoyuanliu/Developer/cs263/proj/FSMSIM/parser/FSMLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u012f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("$\6$\u00d6\n$\r$\16$\u00d7\3%\3%\6%\u00dc\n%\r%\16%\u00dd")
        buf.write("\3&\3&\7&\u00e2\n&\f&\16&\u00e5\13&\3&\3&\3&\7&\u00ea")
        buf.write("\n&\f&\16&\u00ed\13&\3&\5&\u00f0\n&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3*\7*\u00fb\n*\f*\16*\u00fe\13*\3+\3+\3,\3,\3")
        buf.write("-\6-\u0105\n-\r-\16-\u0106\3-\3-\3.\6.\u010c\n.\r.\16")
        buf.write(".\u010d\3.\3.\3/\3/\3/\3/\7/\u0116\n/\f/\16/\u0119\13")
        buf.write("/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\7\60\u0124\n\60\f")
        buf.write("\60\16\60\u0127\13\60\3\60\5\60\u012a\n\60\3\60\3\60\3")
        buf.write("\60\3\60\4\u0117\u0125\2\61\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G\2I\2K%M\2O\2Q\2S&U\2W\2Y\'[(])_*\3\2")
        buf.write("\t\5\2\f\f\17\17$$\5\2\f\f\17\17))\3\2\62;\4\2C\\c|\5")
        buf.write("\2C\\aac|\4\2\f\f\17\17\5\2\13\f\16\17\"\"\2\u0133\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2K\3\2\2\2\2S\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\3a\3\2\2")
        buf.write("\2\5c\3\2\2\2\7e\3\2\2\2\tg\3\2\2\2\13i\3\2\2\2\rk\3\2")
        buf.write("\2\2\17m\3\2\2\2\21o\3\2\2\2\23q\3\2\2\2\25s\3\2\2\2\27")
        buf.write("w\3\2\2\2\31z\3\2\2\2\33}\3\2\2\2\35\u0080\3\2\2\2\37")
        buf.write("\u0083\3\2\2\2!\u0085\3\2\2\2#\u0087\3\2\2\2%\u0089\3")
        buf.write("\2\2\2\'\u008c\3\2\2\2)\u008f\3\2\2\2+\u0091\3\2\2\2-")
        buf.write("\u0093\3\2\2\2/\u0095\3\2\2\2\61\u0097\3\2\2\2\63\u009c")
        buf.write("\3\2\2\2\65\u00a2\3\2\2\2\67\u00a9\3\2\2\29\u00b0\3\2")
        buf.write("\2\2;\u00b6\3\2\2\2=\u00bd\3\2\2\2?\u00c3\3\2\2\2A\u00cb")
        buf.write("\3\2\2\2C\u00cf\3\2\2\2E\u00d2\3\2\2\2G\u00d5\3\2\2\2")
        buf.write("I\u00d9\3\2\2\2K\u00ef\3\2\2\2M\u00f1\3\2\2\2O\u00f3\3")
        buf.write("\2\2\2Q\u00f5\3\2\2\2S\u00f7\3\2\2\2U\u00ff\3\2\2\2W\u0101")
        buf.write("\3\2\2\2Y\u0104\3\2\2\2[\u010b\3\2\2\2]\u0111\3\2\2\2")
        buf.write("_\u011f\3\2\2\2ab\7=\2\2b\4\3\2\2\2cd\7<\2\2d\6\3\2\2")
        buf.write("\2ef\7*\2\2f\b\3\2\2\2gh\7+\2\2h\n\3\2\2\2ij\7}\2\2j\f")
        buf.write("\3\2\2\2kl\7\177\2\2l\16\3\2\2\2mn\7]\2\2n\20\3\2\2\2")
        buf.write("op\7_\2\2p\22\3\2\2\2qr\7&\2\2r\24\3\2\2\2st\7f\2\2tu")
        buf.write("\7g\2\2uv\7n\2\2v\26\3\2\2\2wx\7?\2\2xy\7?\2\2y\30\3\2")
        buf.write("\2\2z{\7#\2\2{|\7?\2\2|\32\3\2\2\2}~\7(\2\2~\177\7(\2")
        buf.write("\2\177\34\3\2\2\2\u0080\u0081\7~\2\2\u0081\u0082\7~\2")
        buf.write("\2\u0082\36\3\2\2\2\u0083\u0084\7#\2\2\u0084 \3\2\2\2")
        buf.write("\u0085\u0086\7\60\2\2\u0086\"\3\2\2\2\u0087\u0088\7.\2")
        buf.write("\2\u0088$\3\2\2\2\u0089\u008a\7>\2\2\u008a\u008b\7/\2")
        buf.write("\2\u008b&\3\2\2\2\u008c\u008d\7/\2\2\u008d\u008e\7@\2")
        buf.write("\2\u008e(\3\2\2\2\u008f\u0090\7?\2\2\u0090*\3\2\2\2\u0091")
        buf.write("\u0092\7-\2\2\u0092,\3\2\2\2\u0093\u0094\7/\2\2\u0094")
        buf.write(".\3\2\2\2\u0095\u0096\7,\2\2\u0096\60\3\2\2\2\u0097\u0098")
        buf.write("\7v\2\2\u0098\u0099\7t\2\2\u0099\u009a\7w\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\62\3\2\2\2\u009c\u009d\7h\2\2\u009d\u009e")
        buf.write("\7c\2\2\u009e\u009f\7n\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1")
        buf.write("\7g\2\2\u00a1\64\3\2\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4")
        buf.write("\7o\2\2\u00a4\u00a5\7r\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\u00a8\7v\2\2\u00a8\66\3\2\2\2\u00a9\u00aa")
        buf.write("\7o\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7f\2\2\u00ac\u00ad")
        buf.write("\7w\2\2\u00ad\u00ae\7n\2\2\u00ae\u00af\7g\2\2\u00af8\3")
        buf.write("\2\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3")
        buf.write("\7r\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7v\2\2\u00b5:\3")
        buf.write("\2\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\u00ba\7r\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc<\3\2\2\2\u00bd\u00be\7u\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2>\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5")
        buf.write("\7p\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8")
        buf.write("\7k\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7n\2\2\u00ca@\3")
        buf.write("\2\2\2\u00cb\u00cc\7h\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7t\2\2\u00ceB\3\2\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1D\3\2\2\2\u00d2\u00d3\5G$\2\u00d3F\3\2\2")
        buf.write("\2\u00d4\u00d6\5Q)\2\u00d5\u00d4\3\2\2\2\u00d6\u00d7\3")
        buf.write("\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8H")
        buf.write("\3\2\2\2\u00d9\u00db\7/\2\2\u00da\u00dc\5Q)\2\u00db\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00deJ\3\2\2\2\u00df\u00e3\7$\2\2\u00e0")
        buf.write("\u00e2\5M\'\2\u00e1\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e6\3")
        buf.write("\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00f0\7$\2\2\u00e7\u00eb")
        buf.write("\7)\2\2\u00e8\u00ea\5O(\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f0\7)\2\2")
        buf.write("\u00ef\u00df\3\2\2\2\u00ef\u00e7\3\2\2\2\u00f0L\3\2\2")
        buf.write("\2\u00f1\u00f2\n\2\2\2\u00f2N\3\2\2\2\u00f3\u00f4\n\3")
        buf.write("\2\2\u00f4P\3\2\2\2\u00f5\u00f6\t\4\2\2\u00f6R\3\2\2\2")
        buf.write("\u00f7\u00fc\5U+\2\u00f8\u00fb\5W,\2\u00f9\u00fb\5Q)\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3")
        buf.write("\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fdT")
        buf.write("\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\t\5\2\2\u0100")
        buf.write("V\3\2\2\2\u0101\u0102\t\6\2\2\u0102X\3\2\2\2\u0103\u0105")
        buf.write("\t\7\2\2\u0104\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106")
        buf.write("\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u0109\b-\2\2\u0109Z\3\2\2\2\u010a\u010c\t\b\2\2")
        buf.write("\u010b\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010b\3")
        buf.write("\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110")
        buf.write("\b.\2\2\u0110\\\3\2\2\2\u0111\u0112\7\61\2\2\u0112\u0113")
        buf.write("\7,\2\2\u0113\u0117\3\2\2\2\u0114\u0116\13\2\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0118\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0118\u011a\3\2\2\2\u0119\u0117\3")
        buf.write("\2\2\2\u011a\u011b\7,\2\2\u011b\u011c\7\61\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d\u011e\b/\2\2\u011e^\3\2\2\2\u011f\u0120")
        buf.write("\7\61\2\2\u0120\u0121\7\61\2\2\u0121\u0125\3\2\2\2\u0122")
        buf.write("\u0124\13\2\2\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2")
        buf.write("\2\u0125\u0126\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0129")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012a\7\17\2\2\u0129")
        buf.write("\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012c\7\f\2\2\u012c\u012d\3\2\2\2\u012d\u012e\b")
        buf.write("\60\2\2\u012e`\3\2\2\2\17\2\u00d7\u00dd\u00e3\u00eb\u00ef")
        buf.write("\u00fa\u00fc\u0106\u010d\u0117\u0125\u0129\3\b\2\2")
        return buf.getvalue()


class FSMLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SEMICOLON = 1
    COLON = 2
    LEFTBRACKET = 3
    RIGHTBRACKET = 4
    LEFTCURLY = 5
    RIGHTCURLY = 6
    LEFTANGLE = 7
    RIGHTANGLE = 8
    DOLLAR = 9
    DEL = 10
    EQ = 11
    NEQ = 12
    AND = 13
    OR = 14
    NOT = 15
    DOT = 16
    COMMA = 17
    LEFTARROW = 18
    RIGHTARROW = 19
    ASSIGN = 20
    PLUS = 21
    MINUS = 22
    TIMES = 23
    TRUE = 24
    FALSE = 25
    IMPORT = 26
    MODULE = 27
    INPUT = 28
    OUTPUT = 29
    STATE = 30
    INITIAL = 31
    FOR = 32
    IN = 33
    INT = 34
    STRING = 35
    ID = 36
    NEWLINE = 37
    WS = 38
    COMMENT = 39
    LINE_COMMENT = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'$'", 
            "'del'", "'=='", "'!='", "'&&'", "'||'", "'!'", "'.'", "','", 
            "'<-'", "'->'", "'='", "'+'", "'-'", "'*'", "'true'", "'false'", 
            "'import'", "'module'", "'input'", "'output'", "'state'", "'initial'", 
            "'for'", "'in'" ]

    symbolicNames = [ "<INVALID>",
            "SEMICOLON", "COLON", "LEFTBRACKET", "RIGHTBRACKET", "LEFTCURLY", 
            "RIGHTCURLY", "LEFTANGLE", "RIGHTANGLE", "DOLLAR", "DEL", "EQ", 
            "NEQ", "AND", "OR", "NOT", "DOT", "COMMA", "LEFTARROW", "RIGHTARROW", 
            "ASSIGN", "PLUS", "MINUS", "TIMES", "TRUE", "FALSE", "IMPORT", 
            "MODULE", "INPUT", "OUTPUT", "STATE", "INITIAL", "FOR", "IN", 
            "INT", "STRING", "ID", "NEWLINE", "WS", "COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "SEMICOLON", "COLON", "LEFTBRACKET", "RIGHTBRACKET", "LEFTCURLY", 
                  "RIGHTCURLY", "LEFTANGLE", "RIGHTANGLE", "DOLLAR", "DEL", 
                  "EQ", "NEQ", "AND", "OR", "NOT", "DOT", "COMMA", "LEFTARROW", 
                  "RIGHTARROW", "ASSIGN", "PLUS", "MINUS", "TIMES", "TRUE", 
                  "FALSE", "IMPORT", "MODULE", "INPUT", "OUTPUT", "STATE", 
                  "INITIAL", "FOR", "IN", "INT", "POSINT", "NEGINT", "STRING", 
                  "DoubleStringCharacter", "SingleStringCharacter", "DIGIT", 
                  "ID", "LETTER", "ID_LETTER", "NEWLINE", "WS", "COMMENT", 
                  "LINE_COMMENT" ]

    grammarFileName = "FSMLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


