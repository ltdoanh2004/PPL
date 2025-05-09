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
        buf.write("\31\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\13\n\2\r\2\16")
        buf.write("\2\f\3\3\6\3\20\n\3\r\3\16\3\21\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\2\2\5\3\3\5\4\7\5\3\2\4\5\2cdfg||\5\2\13\f\17\17\"")
        buf.write("\"\2\32\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3\n\3\2\2")
        buf.write("\2\5\17\3\2\2\2\7\25\3\2\2\2\t\13\t\2\2\2\n\t\3\2\2\2")
        buf.write("\13\f\3\2\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r\4\3\2\2\2\16\20")
        buf.write("\t\3\2\2\17\16\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21")
        buf.write("\22\3\2\2\2\22\23\3\2\2\2\23\24\b\3\2\2\24\6\3\2\2\2\25")
        buf.write("\26\13\2\2\2\26\27\3\2\2\2\27\30\b\4\2\2\30\b\3\2\2\2")
        buf.write("\5\2\f\21\3\b\2\2")
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


