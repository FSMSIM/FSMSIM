# Generated from /Users/haoyuanliu/Developer/cs263/proj/FSMSIM/parser/FSMLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(")
        buf.write("\u0125\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\6\"\u00cc\n\"\r\"\16\"\u00cd")
        buf.write("\3#\3#\6#\u00d2\n#\r#\16#\u00d3\3$\3$\7$\u00d8\n$\f$\16")
        buf.write("$\u00db\13$\3$\3$\3$\7$\u00e0\n$\f$\16$\u00e3\13$\3$\5")
        buf.write("$\u00e6\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\7(\u00f1\n(\f")
        buf.write("(\16(\u00f4\13(\3)\3)\3*\3*\3+\6+\u00fb\n+\r+\16+\u00fc")
        buf.write("\3+\3+\3,\6,\u0102\n,\r,\16,\u0103\3,\3,\3-\3-\3-\3-\7")
        buf.write("-\u010c\n-\f-\16-\u010f\13-\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\7.\u011a\n.\f.\16.\u011d\13.\3.\5.\u0120\n.\3.\3.\3")
        buf.write(".\3.\4\u010d\u011b\2/\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C\2E\2G#I\2K\2M\2O$Q\2S\2U%W&Y\'[(\3\2\t\5\2\f")
        buf.write("\f\17\17$$\5\2\f\f\17\17))\3\2\62;\4\2C\\c|\5\2C\\aac")
        buf.write("|\4\2\f\f\17\17\5\2\13\f\16\17\"\"\2\u0129\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("G\3\2\2\2\2O\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\3]\3\2\2\2\5_\3\2\2\2\7a\3\2\2\2\tc\3\2\2")
        buf.write("\2\13e\3\2\2\2\rg\3\2\2\2\17i\3\2\2\2\21k\3\2\2\2\23m")
        buf.write("\3\2\2\2\25p\3\2\2\2\27s\3\2\2\2\31v\3\2\2\2\33y\3\2\2")
        buf.write("\2\35{\3\2\2\2\37}\3\2\2\2!\177\3\2\2\2#\u0082\3\2\2\2")
        buf.write("%\u0085\3\2\2\2\'\u0087\3\2\2\2)\u0089\3\2\2\2+\u008b")
        buf.write("\3\2\2\2-\u008d\3\2\2\2/\u0092\3\2\2\2\61\u0098\3\2\2")
        buf.write("\2\63\u009f\3\2\2\2\65\u00a6\3\2\2\2\67\u00ac\3\2\2\2")
        buf.write("9\u00b3\3\2\2\2;\u00b9\3\2\2\2=\u00c1\3\2\2\2?\u00c5\3")
        buf.write("\2\2\2A\u00c8\3\2\2\2C\u00cb\3\2\2\2E\u00cf\3\2\2\2G\u00e5")
        buf.write("\3\2\2\2I\u00e7\3\2\2\2K\u00e9\3\2\2\2M\u00eb\3\2\2\2")
        buf.write("O\u00ed\3\2\2\2Q\u00f5\3\2\2\2S\u00f7\3\2\2\2U\u00fa\3")
        buf.write("\2\2\2W\u0101\3\2\2\2Y\u0107\3\2\2\2[\u0115\3\2\2\2]^")
        buf.write("\7=\2\2^\4\3\2\2\2_`\7<\2\2`\6\3\2\2\2ab\7*\2\2b\b\3\2")
        buf.write("\2\2cd\7+\2\2d\n\3\2\2\2ef\7}\2\2f\f\3\2\2\2gh\7\177\2")
        buf.write("\2h\16\3\2\2\2ij\7]\2\2j\20\3\2\2\2kl\7_\2\2l\22\3\2\2")
        buf.write("\2mn\7?\2\2no\7?\2\2o\24\3\2\2\2pq\7#\2\2qr\7?\2\2r\26")
        buf.write("\3\2\2\2st\7(\2\2tu\7(\2\2u\30\3\2\2\2vw\7~\2\2wx\7~\2")
        buf.write("\2x\32\3\2\2\2yz\7#\2\2z\34\3\2\2\2{|\7\60\2\2|\36\3\2")
        buf.write("\2\2}~\7.\2\2~ \3\2\2\2\177\u0080\7>\2\2\u0080\u0081\7")
        buf.write("/\2\2\u0081\"\3\2\2\2\u0082\u0083\7/\2\2\u0083\u0084\7")
        buf.write("@\2\2\u0084$\3\2\2\2\u0085\u0086\7?\2\2\u0086&\3\2\2\2")
        buf.write("\u0087\u0088\7-\2\2\u0088(\3\2\2\2\u0089\u008a\7/\2\2")
        buf.write("\u008a*\3\2\2\2\u008b\u008c\7,\2\2\u008c,\3\2\2\2\u008d")
        buf.write("\u008e\7v\2\2\u008e\u008f\7t\2\2\u008f\u0090\7w\2\2\u0090")
        buf.write("\u0091\7g\2\2\u0091.\3\2\2\2\u0092\u0093\7h\2\2\u0093")
        buf.write("\u0094\7c\2\2\u0094\u0095\7n\2\2\u0095\u0096\7u\2\2\u0096")
        buf.write("\u0097\7g\2\2\u0097\60\3\2\2\2\u0098\u0099\7k\2\2\u0099")
        buf.write("\u009a\7o\2\2\u009a\u009b\7r\2\2\u009b\u009c\7q\2\2\u009c")
        buf.write("\u009d\7t\2\2\u009d\u009e\7v\2\2\u009e\62\3\2\2\2\u009f")
        buf.write("\u00a0\7o\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2\7f\2\2\u00a2")
        buf.write("\u00a3\7w\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7g\2\2\u00a5")
        buf.write("\64\3\2\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8\7p\2\2\u00a8")
        buf.write("\u00a9\7r\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7v\2\2\u00ab")
        buf.write("\66\3\2\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7w\2\2\u00ae")
        buf.write("\u00af\7v\2\2\u00af\u00b0\7r\2\2\u00b0\u00b1\7w\2\2\u00b1")
        buf.write("\u00b2\7v\2\2\u00b28\3\2\2\2\u00b3\u00b4\7u\2\2\u00b4")
        buf.write("\u00b5\7v\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7v\2\2\u00b7")
        buf.write("\u00b8\7g\2\2\u00b8:\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba")
        buf.write("\u00bb\7p\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7v\2\2\u00bd")
        buf.write("\u00be\7k\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0\7n\2\2\u00c0")
        buf.write("<\3\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3\7q\2\2\u00c3")
        buf.write("\u00c4\7t\2\2\u00c4>\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6")
        buf.write("\u00c7\7p\2\2\u00c7@\3\2\2\2\u00c8\u00c9\5C\"\2\u00c9")
        buf.write("B\3\2\2\2\u00ca\u00cc\5M\'\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ceD\3\2\2\2\u00cf\u00d1\7/\2\2\u00d0\u00d2\5M\'\2")
        buf.write("\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1\3")
        buf.write("\2\2\2\u00d3\u00d4\3\2\2\2\u00d4F\3\2\2\2\u00d5\u00d9")
        buf.write("\7$\2\2\u00d6\u00d8\5I%\2\u00d7\u00d6\3\2\2\2\u00d8\u00db")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00e6\7$\2\2")
        buf.write("\u00dd\u00e1\7)\2\2\u00de\u00e0\5K&\2\u00df\u00de\3\2")
        buf.write("\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4")
        buf.write("\u00e6\7)\2\2\u00e5\u00d5\3\2\2\2\u00e5\u00dd\3\2\2\2")
        buf.write("\u00e6H\3\2\2\2\u00e7\u00e8\n\2\2\2\u00e8J\3\2\2\2\u00e9")
        buf.write("\u00ea\n\3\2\2\u00eaL\3\2\2\2\u00eb\u00ec\t\4\2\2\u00ec")
        buf.write("N\3\2\2\2\u00ed\u00f2\5Q)\2\u00ee\u00f1\5S*\2\u00ef\u00f1")
        buf.write("\5M\'\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2")
        buf.write("\u00f3P\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\t\5\2")
        buf.write("\2\u00f6R\3\2\2\2\u00f7\u00f8\t\6\2\2\u00f8T\3\2\2\2\u00f9")
        buf.write("\u00fb\t\7\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\3")
        buf.write("\2\2\2\u00fe\u00ff\b+\2\2\u00ffV\3\2\2\2\u0100\u0102\t")
        buf.write("\b\2\2\u0101\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105\3\2\2\2\u0105")
        buf.write("\u0106\b,\2\2\u0106X\3\2\2\2\u0107\u0108\7\61\2\2\u0108")
        buf.write("\u0109\7,\2\2\u0109\u010d\3\2\2\2\u010a\u010c\13\2\2\2")
        buf.write("\u010b\u010a\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010e\3")
        buf.write("\2\2\2\u010d\u010b\3\2\2\2\u010e\u0110\3\2\2\2\u010f\u010d")
        buf.write("\3\2\2\2\u0110\u0111\7,\2\2\u0111\u0112\7\61\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0114\b-\2\2\u0114Z\3\2\2\2\u0115")
        buf.write("\u0116\7\61\2\2\u0116\u0117\7\61\2\2\u0117\u011b\3\2\2")
        buf.write("\2\u0118\u011a\13\2\2\2\u0119\u0118\3\2\2\2\u011a\u011d")
        buf.write("\3\2\2\2\u011b\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c")
        buf.write("\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u0120\7\17\2")
        buf.write("\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0122\7\f\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("\u0124\b.\2\2\u0124\\\3\2\2\2\17\2\u00cd\u00d3\u00d9\u00e1")
        buf.write("\u00e5\u00f0\u00f2\u00fc\u0103\u010d\u011b\u011f\3\b\2")
        buf.write("\2")
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
    EQ = 9
    NEQ = 10
    AND = 11
    OR = 12
    NOT = 13
    DOT = 14
    COMMA = 15
    LEFTARROW = 16
    RIGHTARROW = 17
    ASSIGN = 18
    PLUS = 19
    MINUS = 20
    TIMES = 21
    TRUE = 22
    FALSE = 23
    IMPORT = 24
    MODULE = 25
    INPUT = 26
    OUTPUT = 27
    STATE = 28
    INITIAL = 29
    FOR = 30
    IN = 31
    INT = 32
    STRING = 33
    ID = 34
    NEWLINE = 35
    WS = 36
    COMMENT = 37
    LINE_COMMENT = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'=='", 
            "'!='", "'&&'", "'||'", "'!'", "'.'", "','", "'<-'", "'->'", 
            "'='", "'+'", "'-'", "'*'", "'true'", "'false'", "'import'", 
            "'module'", "'input'", "'output'", "'state'", "'initial'", "'for'", 
            "'in'" ]

    symbolicNames = [ "<INVALID>",
            "SEMICOLON", "COLON", "LEFTBRACKET", "RIGHTBRACKET", "LEFTCURLY", 
            "RIGHTCURLY", "LEFTANGLE", "RIGHTANGLE", "EQ", "NEQ", "AND", 
            "OR", "NOT", "DOT", "COMMA", "LEFTARROW", "RIGHTARROW", "ASSIGN", 
            "PLUS", "MINUS", "TIMES", "TRUE", "FALSE", "IMPORT", "MODULE", 
            "INPUT", "OUTPUT", "STATE", "INITIAL", "FOR", "IN", "INT", "STRING", 
            "ID", "NEWLINE", "WS", "COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "SEMICOLON", "COLON", "LEFTBRACKET", "RIGHTBRACKET", "LEFTCURLY", 
                  "RIGHTCURLY", "LEFTANGLE", "RIGHTANGLE", "EQ", "NEQ", 
                  "AND", "OR", "NOT", "DOT", "COMMA", "LEFTARROW", "RIGHTARROW", 
                  "ASSIGN", "PLUS", "MINUS", "TIMES", "TRUE", "FALSE", "IMPORT", 
                  "MODULE", "INPUT", "OUTPUT", "STATE", "INITIAL", "FOR", 
                  "IN", "INT", "POSINT", "NEGINT", "STRING", "DoubleStringCharacter", 
                  "SingleStringCharacter", "DIGIT", "ID", "LETTER", "ID_LETTER", 
                  "NEWLINE", "WS", "COMMENT", "LINE_COMMENT" ]

    grammarFileName = "FSMLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


