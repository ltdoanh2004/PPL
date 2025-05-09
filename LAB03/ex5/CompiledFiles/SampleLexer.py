# Generated from Sample.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\6\4&\n\4\r\4\16")
        buf.write("\4\'\3\5\6\5+\n\5\r\5\16\5,\3\5\3\5\2\2\6\3\3\5\4\7\5")
        buf.write("\t\6\3\2\4\3\2c|\5\2\13\f\17\17\"\"\2\63\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5\"\3")
        buf.write("\2\2\2\7%\3\2\2\2\t*\3\2\2\2\13\f\7v\2\2\f\r\7j\2\2\r")
        buf.write("\16\7g\2\2\16\4\3\2\2\2\17\20\7v\2\2\20\21\7w\2\2\21\22")
        buf.write("\7t\2\2\22\23\7p\2\2\23\24\7\"\2\2\24\25\7q\2\2\25#\7")
        buf.write("p\2\2\26\27\7v\2\2\27\30\7w\2\2\30\31\7t\2\2\31\32\7p")
        buf.write("\2\2\32\33\7\"\2\2\33\34\7q\2\2\34\35\7h\2\2\35#\7h\2")
        buf.write("\2\36\37\7r\2\2\37 \7n\2\2 !\7c\2\2!#\7{\2\2\"\17\3\2")
        buf.write("\2\2\"\26\3\2\2\2\"\36\3\2\2\2#\6\3\2\2\2$&\t\2\2\2%$")
        buf.write("\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\b\3\2\2\2)")
        buf.write("+\t\3\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-.\3")
        buf.write("\2\2\2./\b\5\2\2/\n\3\2\2\2\6\2\"\',\3\b\2\2")
        return buf.getvalue()


class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    START = 2
    ID = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'the'" ]

    symbolicNames = [ "<INVALID>",
            "START", "ID", "WS" ]

    ruleNames = [ "T__0", "START", "ID", "WS" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


