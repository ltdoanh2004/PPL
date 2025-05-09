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
        buf.write("\34\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\5")
        buf.write("\3\17\n\3\3\3\3\3\3\4\3\4\3\5\3\5\7\5\27\n\5\f\5\16\5")
        buf.write("\32\13\5\3\5\2\2\6\2\4\6\b\2\2\2\31\2\n\3\2\2\2\4\f\3")
        buf.write("\2\2\2\6\22\3\2\2\2\b\24\3\2\2\2\n\13\5\4\3\2\13\3\3\2")
        buf.write("\2\2\f\16\7\4\2\2\r\17\5\6\4\2\16\r\3\2\2\2\16\17\3\2")
        buf.write("\2\2\17\20\3\2\2\2\20\21\5\b\5\2\21\5\3\2\2\2\22\23\7")
        buf.write("\3\2\2\23\7\3\2\2\2\24\30\7\5\2\2\25\27\7\5\2\2\26\25")
        buf.write("\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\t\3\2\2\2\32\30\3\2\2\2\4\16\30")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'the'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "START", "ID", "WS" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_option = 2
    RULE_compoundID = 3

    ruleNames =  [ "program", "sentence", "option", "compoundID" ]

    EOF = Token.EOF
    T__0=1
    START=2
    ID=3
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
            if _la==SampleParser.T__0:
                self.state = 11
                self.option()


            self.state = 14
            self.compoundID()
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(SampleParser.T__0)
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
            self.state = 18
            self.match(SampleParser.ID)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SampleParser.ID:
                self.state = 19
                self.match(SampleParser.ID)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





