# Generated from Sample.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\r\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\3\3\3\3\2\2\4\2")
        buf.write("\4\2\2\2\n\2\6\3\2\2\2\4\b\3\2\2\2\6\7\5\4\3\2\7\3\3\2")
        buf.write("\2\2\b\t\7\3\2\2\t\n\7\4\2\2\n\13\7\5\2\2\13\5\3\2\2\2")
        buf.write("\2")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'?'" ]

    symbolicNames = [ "<INVALID>", "START", "ID", "E_Mask", "WS" ]

    RULE_program = 0
    RULE_sentence = 1

    ruleNames =  [ "program", "sentence" ]

    EOF = Token.EOF
    START=1
    ID=2
    E_Mask=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self):
            return self.getTypedRuleContext(SampleParser.SentenceContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_program




    def program(self):

        localctx = SampleParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.sentence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(SampleParser.START, 0)

        def ID(self):
            return self.getToken(SampleParser.ID, 0)

        def E_Mask(self):
            return self.getToken(SampleParser.E_Mask, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_sentence




    def sentence(self):

        localctx = SampleParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(SampleParser.START)
            self.state = 7
            self.match(SampleParser.ID)
            self.state = 8
            self.match(SampleParser.E_Mask)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





