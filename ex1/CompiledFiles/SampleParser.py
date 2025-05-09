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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("O\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\5\2\27\n\2\3\3\3\3\3\3\5")
        buf.write("\3\34\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5+\n\5\3\6\3\6\5\6/\n\6\3\6\3\6\3\6\5\6\64")
        buf.write("\n\6\3\6\3\6\3\6\3\6\3\6\5\6;\n\6\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\5\bC\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2\22\26\2R\2\26")
        buf.write("\3\2\2\2\4\30\3\2\2\2\6\35\3\2\2\2\b*\3\2\2\2\n:\3\2\2")
        buf.write("\2\f<\3\2\2\2\16B\3\2\2\2\20D\3\2\2\2\22J\3\2\2\2\24\27")
        buf.write("\5\4\3\2\25\27\5\6\4\2\26\24\3\2\2\2\26\25\3\2\2\2\27")
        buf.write("\3\3\2\2\2\30\31\5\b\5\2\31\33\5\n\6\2\32\34\5\16\b\2")
        buf.write("\33\32\3\2\2\2\33\34\3\2\2\2\34\5\3\2\2\2\35\36\7\3\2")
        buf.write("\2\36\37\5\20\t\2\37 \7\4\2\2 !\5\4\3\2!\7\3\2\2\2\"#")
        buf.write("\7\5\2\2#+\7\6\2\2$%\7\5\2\2%+\7\7\2\2&+\7\b\2\2\'+\7")
        buf.write("\t\2\2(+\7\n\2\2)+\7\13\2\2*\"\3\2\2\2*$\3\2\2\2*&\3\2")
        buf.write("\2\2*\'\3\2\2\2*(\3\2\2\2*)\3\2\2\2+\t\3\2\2\2,.\7\f\2")
        buf.write("\2-/\5\f\7\2.-\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60;\7\r\2")
        buf.write("\2\61\63\7\f\2\2\62\64\5\f\7\2\63\62\3\2\2\2\63\64\3\2")
        buf.write("\2\2\64\65\3\2\2\2\65;\7\16\2\2\66\67\7\17\2\2\678\7\20")
        buf.write("\2\28;\5\f\7\29;\7\21\2\2:,\3\2\2\2:\61\3\2\2\2:\66\3")
        buf.write("\2\2\2:9\3\2\2\2;\13\3\2\2\2<=\t\2\2\2=\r\3\2\2\2>?\7")
        buf.write("\27\2\2?C\7\35\2\2@A\7\30\2\2AC\7\35\2\2B>\3\2\2\2B@\3")
        buf.write("\2\2\2C\17\3\2\2\2DE\7\f\2\2EF\7\31\2\2FG\7\32\2\2GH\7")
        buf.write("\33\2\2HI\5\22\n\2I\21\3\2\2\2JK\7\35\2\2KL\7\34\2\2L")
        buf.write("M\7\35\2\2M\23\3\2\2\2\t\26\33*.\63:B")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'If'", "'then'", "'Turn'", "'on'", "'off'", 
                     "'Set'", "'Increase'", "'Decrease'", "'Play'", "'the'", 
                     "'light'", "'temperature'", "'music'", "'in'", "'brightness'", 
                     "'kitchen'", "'living'", "'bedroom'", "'bathroom'", 
                     "'office'", "'by'", "'to'", "'time'", "'is'", "'after'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "WS" ]

    RULE_command = 0
    RULE_simpleCommand = 1
    RULE_conditionalCommand = 2
    RULE_action = 3
    RULE_deviceObject = 4
    RULE_roomName = 5
    RULE_modifier = 6
    RULE_condition = 7
    RULE_time = 8

    ruleNames =  [ "command", "simpleCommand", "conditionalCommand", "action", 
                   "deviceObject", "roomName", "modifier", "condition", 
                   "time" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    INT=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleCommand(self):
            return self.getTypedRuleContext(SampleParser.SimpleCommandContext,0)


        def conditionalCommand(self):
            return self.getTypedRuleContext(SampleParser.ConditionalCommandContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_command




    def command(self):

        localctx = SampleParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SampleParser.T__2, SampleParser.T__5, SampleParser.T__6, SampleParser.T__7, SampleParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.simpleCommand()
                pass
            elif token in [SampleParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.conditionalCommand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(SampleParser.ActionContext,0)


        def deviceObject(self):
            return self.getTypedRuleContext(SampleParser.DeviceObjectContext,0)


        def modifier(self):
            return self.getTypedRuleContext(SampleParser.ModifierContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_simpleCommand




    def simpleCommand(self):

        localctx = SampleParser.SimpleCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_simpleCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.action()
            self.state = 23
            self.deviceObject()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SampleParser.T__20 or _la==SampleParser.T__21:
                self.state = 24
                self.modifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(SampleParser.ConditionContext,0)


        def simpleCommand(self):
            return self.getTypedRuleContext(SampleParser.SimpleCommandContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_conditionalCommand




    def conditionalCommand(self):

        localctx = SampleParser.ConditionalCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditionalCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(SampleParser.T__0)
            self.state = 28
            self.condition()
            self.state = 29
            self.match(SampleParser.T__1)
            self.state = 30
            self.simpleCommand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SampleParser.RULE_action




    def action(self):

        localctx = SampleParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_action)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(SampleParser.T__2)
                self.state = 33
                self.match(SampleParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(SampleParser.T__2)
                self.state = 35
                self.match(SampleParser.T__4)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.match(SampleParser.T__5)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.match(SampleParser.T__6)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.match(SampleParser.T__7)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 39
                self.match(SampleParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeviceObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def roomName(self):
            return self.getTypedRuleContext(SampleParser.RoomNameContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_deviceObject




    def deviceObject(self):

        localctx = SampleParser.DeviceObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_deviceObject)
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(SampleParser.T__9)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.T__15) | (1 << SampleParser.T__16) | (1 << SampleParser.T__17) | (1 << SampleParser.T__18) | (1 << SampleParser.T__19))) != 0):
                    self.state = 43
                    self.roomName()


                self.state = 46
                self.match(SampleParser.T__10)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(SampleParser.T__9)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.T__15) | (1 << SampleParser.T__16) | (1 << SampleParser.T__17) | (1 << SampleParser.T__18) | (1 << SampleParser.T__19))) != 0):
                    self.state = 48
                    self.roomName()


                self.state = 51
                self.match(SampleParser.T__11)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(SampleParser.T__12)
                self.state = 53
                self.match(SampleParser.T__13)
                self.state = 54
                self.roomName()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.match(SampleParser.T__14)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoomNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SampleParser.RULE_roomName




    def roomName(self):

        localctx = SampleParser.RoomNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_roomName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.T__15) | (1 << SampleParser.T__16) | (1 << SampleParser.T__17) | (1 << SampleParser.T__18) | (1 << SampleParser.T__19))) != 0)):
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


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SampleParser.INT, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_modifier




    def modifier(self):

        localctx = SampleParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_modifier)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SampleParser.T__20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(SampleParser.T__20)
                self.state = 61
                self.match(SampleParser.INT)
                pass
            elif token in [SampleParser.T__21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(SampleParser.T__21)
                self.state = 63
                self.match(SampleParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def time(self):
            return self.getTypedRuleContext(SampleParser.TimeContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_condition




    def condition(self):

        localctx = SampleParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(SampleParser.T__9)
            self.state = 67
            self.match(SampleParser.T__22)
            self.state = 68
            self.match(SampleParser.T__23)
            self.state = 69
            self.match(SampleParser.T__24)
            self.state = 70
            self.time()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SampleParser.INT)
            else:
                return self.getToken(SampleParser.INT, i)

        def getRuleIndex(self):
            return SampleParser.RULE_time




    def time(self):

        localctx = SampleParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(SampleParser.INT)
            self.state = 73
            self.match(SampleParser.T__25)
            self.state = 74
            self.match(SampleParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





