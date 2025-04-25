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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\5\2!\n\2\3\3\3\3\3\3\5\3&\n\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5/\n\5\3\6\3\6\3\6\3\6\5")
        buf.write("\6\65\n\6\3\7\3\7\7\79\n\7\f\7\16\7<\13\7\3\7\3\7\3\b")
        buf.write("\3\b\7\bB\n\b\f\b\16\bE\13\b\3\b\3\b\3\t\3\t\3\t\3\t\5")
        buf.write("\tM\n\t\3\t\6\tP\n\t\r\t\16\tQ\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\2\4\3\2\13\f\3\2\20\22\2b\2 \3\2\2\2\4\"\3\2\2\2\6")
        buf.write("\'\3\2\2\2\b,\3\2\2\2\n\64\3\2\2\2\f\66\3\2\2\2\16?\3")
        buf.write("\2\2\2\20H\3\2\2\2\22S\3\2\2\2\24U\3\2\2\2\26X\3\2\2\2")
        buf.write("\30Z\3\2\2\2\32`\3\2\2\2\34d\3\2\2\2\36!\5\4\3\2\37!\5")
        buf.write("\6\4\2 \36\3\2\2\2 \37\3\2\2\2!\3\3\2\2\2\"#\5\b\5\2#")
        buf.write("%\5\n\6\2$&\5\24\13\2%$\3\2\2\2%&\3\2\2\2&\5\3\2\2\2\'")
        buf.write("(\7\3\2\2()\5\26\f\2)*\7\4\2\2*+\5\4\3\2+\7\3\2\2\2,.")
        buf.write("\7\23\2\2-/\7\24\2\2.-\3\2\2\2./\3\2\2\2/\t\3\2\2\2\60")
        buf.write("\65\5\f\7\2\61\65\5\16\b\2\62\65\5\20\t\2\63\65\5\22\n")
        buf.write("\2\64\60\3\2\2\2\64\61\3\2\2\2\64\62\3\2\2\2\64\63\3\2")
        buf.write("\2\2\65\13\3\2\2\2\66:\7\5\2\2\679\7\25\2\28\67\3\2\2")
        buf.write("\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<:\3\2\2\2=")
        buf.write(">\7\6\2\2>\r\3\2\2\2?C\7\5\2\2@B\7\25\2\2A@\3\2\2\2BE")
        buf.write("\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2EC\3\2\2\2FG\7\7")
        buf.write("\2\2G\17\3\2\2\2HL\7\b\2\2IM\7\t\2\2JK\7\t\2\2KM\7\5\2")
        buf.write("\2LI\3\2\2\2LJ\3\2\2\2MO\3\2\2\2NP\7\25\2\2ON\3\2\2\2")
        buf.write("PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\21\3\2\2\2ST\7\n\2\2T")
        buf.write("\23\3\2\2\2UV\t\2\2\2VW\7\26\2\2W\25\3\2\2\2XY\5\30\r")
        buf.write("\2Y\27\3\2\2\2Z[\7\5\2\2[\\\7\r\2\2\\]\7\16\2\2]^\5\34")
        buf.write("\17\2^_\5\32\16\2_\31\3\2\2\2`a\7\26\2\2ab\7\17\2\2bc")
        buf.write("\7\26\2\2c\33\3\2\2\2de\t\3\2\2e\35\3\2\2\2\n %.\64:C")
        buf.write("LQ")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'If'", "'then'", "'the'", "'light'", 
                     "'temperature'", "'music'", "'in'", "'brightness'", 
                     "'by'", "'to'", "'time'", "'is'", "':'", "'before'", 
                     "'after'", "'at'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VERB", "PREPOSITION", "WORD", "INT", 
                      "WS" ]

    RULE_command = 0
    RULE_simpleCommand = 1
    RULE_conditionalCommand = 2
    RULE_action = 3
    RULE_deviceObject = 4
    RULE_lightDevice = 5
    RULE_temperatureDevice = 6
    RULE_musicDevice = 7
    RULE_brightnessDevice = 8
    RULE_modifier = 9
    RULE_condition = 10
    RULE_timeCondition = 11
    RULE_time = 12
    RULE_comparator = 13

    ruleNames =  [ "command", "simpleCommand", "conditionalCommand", "action", 
                   "deviceObject", "lightDevice", "temperatureDevice", "musicDevice", 
                   "brightnessDevice", "modifier", "condition", "timeCondition", 
                   "time", "comparator" ]

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
    VERB=17
    PREPOSITION=18
    WORD=19
    INT=20
    WS=21

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
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SampleParser.VERB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.simpleCommand()
                pass
            elif token in [SampleParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
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
            self.state = 32
            self.action()
            self.state = 33
            self.deviceObject()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SampleParser.T__8 or _la==SampleParser.T__9:
                self.state = 34
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
            self.state = 37
            self.match(SampleParser.T__0)
            self.state = 38
            self.condition()
            self.state = 39
            self.match(SampleParser.T__1)
            self.state = 40
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

        def VERB(self):
            return self.getToken(SampleParser.VERB, 0)

        def PREPOSITION(self):
            return self.getToken(SampleParser.PREPOSITION, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_action




    def action(self):

        localctx = SampleParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(SampleParser.VERB)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SampleParser.PREPOSITION:
                self.state = 43
                self.match(SampleParser.PREPOSITION)


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

        def lightDevice(self):
            return self.getTypedRuleContext(SampleParser.LightDeviceContext,0)


        def temperatureDevice(self):
            return self.getTypedRuleContext(SampleParser.TemperatureDeviceContext,0)


        def musicDevice(self):
            return self.getTypedRuleContext(SampleParser.MusicDeviceContext,0)


        def brightnessDevice(self):
            return self.getTypedRuleContext(SampleParser.BrightnessDeviceContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_deviceObject




    def deviceObject(self):

        localctx = SampleParser.DeviceObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_deviceObject)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.lightDevice()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.temperatureDevice()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.musicDevice()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.brightnessDevice()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LightDeviceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SampleParser.WORD)
            else:
                return self.getToken(SampleParser.WORD, i)

        def getRuleIndex(self):
            return SampleParser.RULE_lightDevice




    def lightDevice(self):

        localctx = SampleParser.LightDeviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lightDevice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SampleParser.T__2)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SampleParser.WORD:
                self.state = 53
                self.match(SampleParser.WORD)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(SampleParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemperatureDeviceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SampleParser.WORD)
            else:
                return self.getToken(SampleParser.WORD, i)

        def getRuleIndex(self):
            return SampleParser.RULE_temperatureDevice




    def temperatureDevice(self):

        localctx = SampleParser.TemperatureDeviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_temperatureDevice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(SampleParser.T__2)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SampleParser.WORD:
                self.state = 62
                self.match(SampleParser.WORD)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(SampleParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MusicDeviceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SampleParser.WORD)
            else:
                return self.getToken(SampleParser.WORD, i)

        def getRuleIndex(self):
            return SampleParser.RULE_musicDevice




    def musicDevice(self):

        localctx = SampleParser.MusicDeviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_musicDevice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(SampleParser.T__5)
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 71
                self.match(SampleParser.T__6)
                pass

            elif la_ == 2:
                self.state = 72
                self.match(SampleParser.T__6)
                self.state = 73
                self.match(SampleParser.T__2)
                pass


            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.match(SampleParser.WORD)
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SampleParser.WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BrightnessDeviceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SampleParser.RULE_brightnessDevice




    def brightnessDevice(self):

        localctx = SampleParser.BrightnessDeviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_brightnessDevice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SampleParser.T__7)
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
        self.enterRule(localctx, 18, self.RULE_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not(_la==SampleParser.T__8 or _la==SampleParser.T__9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 84
            self.match(SampleParser.INT)
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

        def timeCondition(self):
            return self.getTypedRuleContext(SampleParser.TimeConditionContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_condition




    def condition(self):

        localctx = SampleParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.timeCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparator(self):
            return self.getTypedRuleContext(SampleParser.ComparatorContext,0)


        def time(self):
            return self.getTypedRuleContext(SampleParser.TimeContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_timeCondition




    def timeCondition(self):

        localctx = SampleParser.TimeConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_timeCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(SampleParser.T__2)
            self.state = 89
            self.match(SampleParser.T__10)
            self.state = 90
            self.match(SampleParser.T__11)
            self.state = 91
            self.comparator()
            self.state = 92
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
        self.enterRule(localctx, 24, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(SampleParser.INT)
            self.state = 95
            self.match(SampleParser.T__12)
            self.state = 96
            self.match(SampleParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SampleParser.RULE_comparator




    def comparator(self):

        localctx = SampleParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.T__13) | (1 << SampleParser.T__14) | (1 << SampleParser.T__15))) != 0)):
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





