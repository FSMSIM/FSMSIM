# Generated from /Users/haoyuanliu/Developer/cs263/proj/FSMSIM/parser/FSMLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(")
        buf.write("\u0121\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\6\"\u00ca\n\"\r\"\16\"\u00cb\3#\3")
        buf.write("#\6#\u00d0\n#\r#\16#\u00d1\3$\3$\7$\u00d6\n$\f$\16$\u00d9")
        buf.write("\13$\3$\3$\3$\7$\u00de\n$\f$\16$\u00e1\13$\3$\5$\u00e4")
        buf.write("\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\7(\u00ef\n(\f(\16(\u00f2")
        buf.write("\13(\3)\3)\3*\6*\u00f7\n*\r*\16*\u00f8\3*\3*\3+\6+\u00fe")
        buf.write("\n+\r+\16+\u00ff\3+\3+\3,\3,\3,\3,\7,\u0108\n,\f,\16,")
        buf.write("\u010b\13,\3,\3,\3,\3,\3,\3-\3-\3-\3-\7-\u0116\n-\f-\16")
        buf.write("-\u0119\13-\3-\5-\u011c\n-\3-\3-\3-\3-\4\u0109\u0117\2")
        buf.write(".\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C\2E\2G#I\2K\2")
        buf.write("M\2O$Q\2S%U&W\'Y(\3\2\b\5\2\f\f\17\17$$\5\2\f\f\17\17")
        buf.write("))\3\2\62;\5\2C\\aac|\4\2\f\f\17\17\5\2\13\f\16\17\"\"")
        buf.write("\2\u0126\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2G\3\2\2\2\2O\3\2\2\2\2S\3\2\2\2")
        buf.write("\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\3[\3\2\2\2\5]\3\2\2")
        buf.write("\2\7_\3\2\2\2\ta\3\2\2\2\13c\3\2\2\2\re\3\2\2\2\17g\3")
        buf.write("\2\2\2\21i\3\2\2\2\23k\3\2\2\2\25n\3\2\2\2\27q\3\2\2\2")
        buf.write("\31t\3\2\2\2\33w\3\2\2\2\35y\3\2\2\2\37{\3\2\2\2!}\3\2")
        buf.write("\2\2#\u0080\3\2\2\2%\u0083\3\2\2\2\'\u0085\3\2\2\2)\u0087")
        buf.write("\3\2\2\2+\u0089\3\2\2\2-\u008b\3\2\2\2/\u0090\3\2\2\2")
        buf.write("\61\u0096\3\2\2\2\63\u009d\3\2\2\2\65\u00a4\3\2\2\2\67")
        buf.write("\u00aa\3\2\2\29\u00b1\3\2\2\2;\u00b7\3\2\2\2=\u00bf\3")
        buf.write("\2\2\2?\u00c3\3\2\2\2A\u00c6\3\2\2\2C\u00c9\3\2\2\2E\u00cd")
        buf.write("\3\2\2\2G\u00e3\3\2\2\2I\u00e5\3\2\2\2K\u00e7\3\2\2\2")
        buf.write("M\u00e9\3\2\2\2O\u00eb\3\2\2\2Q\u00f3\3\2\2\2S\u00f6\3")
        buf.write("\2\2\2U\u00fd\3\2\2\2W\u0103\3\2\2\2Y\u0111\3\2\2\2[\\")
        buf.write("\7=\2\2\\\4\3\2\2\2]^\7<\2\2^\6\3\2\2\2_`\7*\2\2`\b\3")
        buf.write("\2\2\2ab\7+\2\2b\n\3\2\2\2cd\7}\2\2d\f\3\2\2\2ef\7\177")
        buf.write("\2\2f\16\3\2\2\2gh\7]\2\2h\20\3\2\2\2ij\7_\2\2j\22\3\2")
        buf.write("\2\2kl\7?\2\2lm\7?\2\2m\24\3\2\2\2no\7#\2\2op\7?\2\2p")
        buf.write("\26\3\2\2\2qr\7(\2\2rs\7(\2\2s\30\3\2\2\2tu\7~\2\2uv\7")
        buf.write("~\2\2v\32\3\2\2\2wx\7#\2\2x\34\3\2\2\2yz\7\60\2\2z\36")
        buf.write("\3\2\2\2{|\7.\2\2| \3\2\2\2}~\7>\2\2~\177\7/\2\2\177\"")
        buf.write("\3\2\2\2\u0080\u0081\7/\2\2\u0081\u0082\7@\2\2\u0082$")
        buf.write("\3\2\2\2\u0083\u0084\7?\2\2\u0084&\3\2\2\2\u0085\u0086")
        buf.write("\7-\2\2\u0086(\3\2\2\2\u0087\u0088\7/\2\2\u0088*\3\2\2")
        buf.write("\2\u0089\u008a\7,\2\2\u008a,\3\2\2\2\u008b\u008c\7v\2")
        buf.write("\2\u008c\u008d\7t\2\2\u008d\u008e\7w\2\2\u008e\u008f\7")
        buf.write("g\2\2\u008f.\3\2\2\2\u0090\u0091\7h\2\2\u0091\u0092\7")
        buf.write("c\2\2\u0092\u0093\7n\2\2\u0093\u0094\7u\2\2\u0094\u0095")
        buf.write("\7g\2\2\u0095\60\3\2\2\2\u0096\u0097\7k\2\2\u0097\u0098")
        buf.write("\7o\2\2\u0098\u0099\7r\2\2\u0099\u009a\7q\2\2\u009a\u009b")
        buf.write("\7t\2\2\u009b\u009c\7v\2\2\u009c\62\3\2\2\2\u009d\u009e")
        buf.write("\7o\2\2\u009e\u009f\7q\2\2\u009f\u00a0\7f\2\2\u00a0\u00a1")
        buf.write("\7w\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3\7g\2\2\u00a3\64")
        buf.write("\3\2\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7")
        buf.write("\7r\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7v\2\2\u00a9\66")
        buf.write("\3\2\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\u00ae\7r\2\2\u00ae\u00af\7w\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b08\3\2\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3")
        buf.write("\7v\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6:\3\2\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9")
        buf.write("\7p\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\7k\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7n\2\2\u00be<\3")
        buf.write("\2\2\2\u00bf\u00c0\7h\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2>\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5")
        buf.write("\7p\2\2\u00c5@\3\2\2\2\u00c6\u00c7\5C\"\2\u00c7B\3\2\2")
        buf.write("\2\u00c8\u00ca\5M\'\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb")
        buf.write("\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc")
        buf.write("D\3\2\2\2\u00cd\u00cf\7/\2\2\u00ce\u00d0\5M\'\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2F\3\2\2\2\u00d3\u00d7\7$\2\2")
        buf.write("\u00d4\u00d6\5I%\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3\2")
        buf.write("\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00e4\7$\2\2\u00db")
        buf.write("\u00df\7)\2\2\u00dc\u00de\5K&\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e4\7")
        buf.write(")\2\2\u00e3\u00d3\3\2\2\2\u00e3\u00db\3\2\2\2\u00e4H\3")
        buf.write("\2\2\2\u00e5\u00e6\n\2\2\2\u00e6J\3\2\2\2\u00e7\u00e8")
        buf.write("\n\3\2\2\u00e8L\3\2\2\2\u00e9\u00ea\t\4\2\2\u00eaN\3\2")
        buf.write("\2\2\u00eb\u00f0\5Q)\2\u00ec\u00ef\5Q)\2\u00ed\u00ef\5")
        buf.write("M\'\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f2")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write("P\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\t\5\2\2\u00f4")
        buf.write("R\3\2\2\2\u00f5\u00f7\t\6\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fa\3\2\2\2\u00fa\u00fb\b*\2\2\u00fbT\3\2\2\2")
        buf.write("\u00fc\u00fe\t\7\2\2\u00fd\u00fc\3\2\2\2\u00fe\u00ff\3")
        buf.write("\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101")
        buf.write("\3\2\2\2\u0101\u0102\b+\2\2\u0102V\3\2\2\2\u0103\u0104")
        buf.write("\7\61\2\2\u0104\u0105\7,\2\2\u0105\u0109\3\2\2\2\u0106")
        buf.write("\u0108\13\2\2\2\u0107\u0106\3\2\2\2\u0108\u010b\3\2\2")
        buf.write("\2\u0109\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010c")
        buf.write("\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d\7,\2\2\u010d")
        buf.write("\u010e\7\61\2\2\u010e\u010f\3\2\2\2\u010f\u0110\b,\2\2")
        buf.write("\u0110X\3\2\2\2\u0111\u0112\7\61\2\2\u0112\u0113\7\61")
        buf.write("\2\2\u0113\u0117\3\2\2\2\u0114\u0116\13\2\2\2\u0115\u0114")
        buf.write("\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0118\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2")
        buf.write("\u011a\u011c\7\17\2\2\u011b\u011a\3\2\2\2\u011b\u011c")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\7\f\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f\u0120\b-\2\2\u0120Z\3\2\2\2\17\2")
        buf.write("\u00cb\u00d1\u00d7\u00df\u00e3\u00ee\u00f0\u00f8\u00ff")
        buf.write("\u0109\u0117\u011b\3\b\2\2")
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
                  "SingleStringCharacter", "DIGIT", "ID", "ID_LETTER", "NEWLINE", 
                  "WS", "COMMENT", "LINE_COMMENT" ]

    grammarFileName = "FSMLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


