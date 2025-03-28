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
        buf.write(")\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\5\2\25\n\2\3\2\3\2\6\2\31\n\2\r\2")
        buf.write("\16\2\32\3\2\3\2\3\3\6\3 \n\3\r\3\16\3!\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2\4\3\2c|\5\2\13\f\17\17")
        buf.write("\"\"\2-\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3\24\3\2\2")
        buf.write("\2\5\37\3\2\2\2\7%\3\2\2\2\t\n\7F\2\2\n\25\7q\2\2\13\f")
        buf.write("\7F\2\2\f\r\7q\2\2\r\16\7g\2\2\16\25\7u\2\2\17\20\7C\2")
        buf.write("\2\20\21\7t\2\2\21\25\7g\2\2\22\23\7K\2\2\23\25\7u\2\2")
        buf.write("\24\t\3\2\2\2\24\13\3\2\2\2\24\17\3\2\2\2\24\22\3\2\2")
        buf.write("\2\25\26\3\2\2\2\26\30\7\"\2\2\27\31\t\2\2\2\30\27\3\2")
        buf.write("\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\34\3")
        buf.write("\2\2\2\34\35\7A\2\2\35\4\3\2\2\2\36 \t\3\2\2\37\36\3\2")
        buf.write("\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\b\3")
        buf.write("\2\2$\6\3\2\2\2%&\13\2\2\2&\'\3\2\2\2\'(\b\4\2\2(\b\3")
        buf.write("\2\2\2\6\2\24\32!\3\b\2\2")
        return buf.getvalue()


class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    QUESTION = 1
    WS = 2
    ERROR_CHAR = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "QUESTION", "WS", "ERROR_CHAR" ]

    ruleNames = [ "QUESTION", "WS", "ERROR_CHAR" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


