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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\36\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\7")
        buf.write("\2\17\n\2\f\2\16\2\22\13\2\3\3\6\3\25\n\3\r\3\16\3\26")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2\4\5\2c")
        buf.write("dfg||\5\2\13\f\17\17\"\"\2\37\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\3\t\3\2\2\2\5\24\3\2\2\2\7\32\3\2\2\2\t\n")
        buf.write("\7c\2\2\n\13\7d\2\2\13\f\7e\2\2\f\20\3\2\2\2\r\17\t\2")
        buf.write("\2\2\16\r\3\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20\21\3")
        buf.write("\2\2\2\21\4\3\2\2\2\22\20\3\2\2\2\23\25\t\3\2\2\24\23")
        buf.write("\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27")
        buf.write("\30\3\2\2\2\30\31\b\3\2\2\31\6\3\2\2\2\32\33\13\2\2\2")
        buf.write("\33\34\3\2\2\2\34\35\b\4\2\2\35\b\3\2\2\2\5\2\20\26\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    WS = 2
    ERROR_CHAR = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "ID", "WS", "ERROR_CHAR" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


