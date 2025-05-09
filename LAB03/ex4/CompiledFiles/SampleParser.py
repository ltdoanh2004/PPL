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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\32\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\5")
        buf.write("\3\17\n\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\5\5\30\n\5\3\5\2")
        buf.write("\2\6\2\4\6\b\2\3\3\2\3\5\2\27\2\n\3\2\2\2\4\f\3\2\2\2")
        buf.write("\6\23\3\2\2\2\b\25\3\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f")
        buf.write("\16\7\6\2\2\r\17\5\6\4\2\16\r\3\2\2\2\16\17\3\2\2\2\17")
        buf.write("\20\3\2\2\2\20\21\5\b\5\2\21\22\7\7\2\2\22\5\3\2\2\2\23")
        buf.write("\24\t\2\2\2\24\7\3\2\2\2\25\27\7\b\2\2\26\30\7\b\2\2\27")
        buf.write("\26\3\2\2\2\27\30\3\2\2\2\30\t\3\2\2\2\4\16\27")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'an'", "'the'", "<INVALID>", "'?'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "START", "E_Mask", "ID", "WS" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_option = 2
    RULE_compoundID = 3

    ruleNames =  [ "program", "sentence", "option", "compoundID" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    START=4
    E_Mask=5
    ID=6
    WS=7

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
            self.state = 8
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

        def compoundID(self):
            return self.getTypedRuleContext(SampleParser.CompoundIDContext,0)


        def E_Mask(self):
            return self.getToken(SampleParser.E_Mask, 0)

        def option(self):
            return self.getTypedRuleContext(SampleParser.OptionContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_sentence




    def sentence(self):

        localctx = SampleParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(SampleParser.START)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.T__0) | (1 << SampleParser.T__1) | (1 << SampleParser.T__2))) != 0):
                self.state = 11
                self.option()


            self.state = 14
            self.compoundID()
            self.state = 15
            self.match(SampleParser.E_Mask)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SampleParser.RULE_option




    def option(self):

        localctx = SampleParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_option)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.T__0) | (1 << SampleParser.T__1) | (1 << SampleParser.T__2))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SampleParser.ID)
            else:
                return self.getToken(SampleParser.ID, i)

        def getRuleIndex(self):
            return SampleParser.RULE_compoundID




    def compoundID(self):

        localctx = SampleParser.CompoundIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compoundID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(SampleParser.ID)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SampleParser.ID:
                self.state = 20
                self.match(SampleParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





