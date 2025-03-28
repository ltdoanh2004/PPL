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
        buf.write(")\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\r\n\2\f")
        buf.write("\2\16\2\20\13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\5\2\35\n\2\3\3\6\3 \n\3\r\3\16\3!\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2\5\3\2c|\5\2\62;aac|\5")
        buf.write("\2\13\f\17\17\"\"\2,\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\3\t\3\2\2\2\5\37\3\2\2\2\7%\3\2\2\2\t\n\t\2\2\2\n\16")
        buf.write("\t\2\2\2\13\r\t\3\2\2\f\13\3\2\2\2\r\20\3\2\2\2\16\f\3")
        buf.write("\2\2\2\16\17\3\2\2\2\17\34\3\2\2\2\20\16\3\2\2\2\21\22")
        buf.write("\7q\2\2\22\35\7m\2\2\23\24\7h\2\2\24\25\7c\2\2\25\26\7")
        buf.write("k\2\2\26\35\7n\2\2\27\30\7o\2\2\30\31\7c\2\2\31\32\7{")
        buf.write("\2\2\32\33\7d\2\2\33\35\7g\2\2\34\21\3\2\2\2\34\23\3\2")
        buf.write("\2\2\34\27\3\2\2\2\35\4\3\2\2\2\36 \t\4\2\2\37\36\3\2")
        buf.write("\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\b\3")
        buf.write("\2\2$\6\3\2\2\2%&\13\2\2\2&\'\3\2\2\2\'(\b\4\2\2(\b\3")
        buf.write("\2\2\2\6\2\16\34!\3\b\2\2")
        return buf.getvalue()


class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VALID_INPUT = 1
    WS = 2
    ERROR_CHAR = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "VALID_INPUT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "VALID_INPUT", "WS", "ERROR_CHAR" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


