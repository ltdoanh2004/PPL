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
        buf.write("\31\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\5\6\5\24\n\5\r\5\16\5\25\3\5\3\5\2\2")
        buf.write("\6\3\3\5\4\7\5\t\6\3\2\4\3\2c|\5\2\13\f\17\17\"\"\2\31")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13")
        buf.write("\3\2\2\2\5\16\3\2\2\2\7\20\3\2\2\2\t\23\3\2\2\2\13\f\7")
        buf.write("K\2\2\f\r\7u\2\2\r\4\3\2\2\2\16\17\t\2\2\2\17\6\3\2\2")
        buf.write("\2\20\21\7A\2\2\21\b\3\2\2\2\22\24\t\3\2\2\23\22\3\2\2")
        buf.write("\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\27\3\2")
        buf.write("\2\2\27\30\b\5\2\2\30\n\3\2\2\2\4\2\25\3\b\2\2")
        return buf.getvalue()


class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IS = 1
    ID = 2
    E_Mask = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Is'", "'?'" ]

    symbolicNames = [ "<INVALID>",
            "IS", "ID", "E_Mask", "WS" ]

    ruleNames = [ "IS", "ID", "E_Mask", "WS" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


