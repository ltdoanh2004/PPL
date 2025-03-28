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
        buf.write("\37\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\13\n\2\r\2\16")
        buf.write("\2\f\3\2\3\2\6\2\21\n\2\r\2\16\2\22\3\3\6\3\26\n\3\r\3")
        buf.write("\16\3\27\3\3\3\3\3\4\3\4\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2")
        buf.write("\4\3\2\62;\5\2\13\f\17\17\"\"\2!\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\3\n\3\2\2\2\5\25\3\2\2\2\7\33\3\2\2\2\t")
        buf.write("\13\t\2\2\2\n\t\3\2\2\2\13\f\3\2\2\2\f\n\3\2\2\2\f\r\3")
        buf.write("\2\2\2\r\16\3\2\2\2\16\20\7\60\2\2\17\21\t\2\2\2\20\17")
        buf.write("\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\4\3\2\2\2\24\26\t\3\2\2\25\24\3\2\2\2\26\27\3\2\2\2\27")
        buf.write("\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\32\b\3\2\2")
        buf.write("\32\6\3\2\2\2\33\34\13\2\2\2\34\35\3\2\2\2\35\36\b\4\2")
        buf.write("\2\36\b\3\2\2\2\6\2\f\22\27\3\b\2\2")
        return buf.getvalue()


class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    FLOAT = 1
    WS = 2
    ERROR_CHAR = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "FLOAT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "FLOAT", "WS", "ERROR_CHAR" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


