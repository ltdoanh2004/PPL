# Generated from /Users/doa_ai/Developer/Poem_PPL/src/PPL/PoemDSL.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,3,0,18,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,40,8,3,1,4,1,4,1,4,1,
        4,3,4,46,8,4,1,5,1,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,0,51,0,17,
        1,0,0,0,2,19,1,0,0,0,4,28,1,0,0,0,6,39,1,0,0,0,8,45,1,0,0,0,10,47,
        1,0,0,0,12,18,3,2,1,0,13,18,3,4,2,0,14,18,3,6,3,0,15,18,3,8,4,0,
        16,18,3,10,5,0,17,12,1,0,0,0,17,13,1,0,0,0,17,14,1,0,0,0,17,15,1,
        0,0,0,17,16,1,0,0,0,18,1,1,0,0,0,19,20,5,1,0,0,20,21,5,2,0,0,21,
        22,5,3,0,0,22,23,5,14,0,0,23,24,5,4,0,0,24,25,5,15,0,0,25,26,5,5,
        0,0,26,27,5,14,0,0,27,3,1,0,0,0,28,29,5,1,0,0,29,30,5,6,0,0,30,31,
        5,2,0,0,31,32,5,4,0,0,32,33,5,15,0,0,33,34,5,7,0,0,34,35,5,14,0,
        0,35,5,1,0,0,0,36,40,5,8,0,0,37,38,5,9,0,0,38,40,5,10,0,0,39,36,
        1,0,0,0,39,37,1,0,0,0,40,7,1,0,0,0,41,42,5,11,0,0,42,46,5,12,0,0,
        43,44,5,9,0,0,44,46,5,12,0,0,45,41,1,0,0,0,45,43,1,0,0,0,46,9,1,
        0,0,0,47,48,5,9,0,0,48,49,5,3,0,0,49,50,5,13,0,0,50,11,1,0,0,0,3,
        17,39,45
    ]

class PoemDSLParser ( Parser ):

    grammarFileName = "PoemDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'POEM'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'CONTROLLED'", "<INVALID>", "'HELP'", 
                     "'SHOW'", "'COMMANDS'", "'LIST'", "'TOPICS'", "'INFO'" ]

    symbolicNames = [ "<INVALID>", "GENERATE", "POEM", "MODEL", "CONTEXT", 
                      "STANZAS", "CONTROLLED", "TOPIC", "HELP", "SHOW", 
                      "COMMANDS", "LIST", "TOPICS", "INFO", "INT", "STRING", 
                      "WS" ]

    RULE_command = 0
    RULE_generatePoem = 1
    RULE_generateControlledPoem = 2
    RULE_helpCommand = 3
    RULE_listTopics = 4
    RULE_showModelInfo = 5

    ruleNames =  [ "command", "generatePoem", "generateControlledPoem", 
                   "helpCommand", "listTopics", "showModelInfo" ]

    EOF = Token.EOF
    GENERATE=1
    POEM=2
    MODEL=3
    CONTEXT=4
    STANZAS=5
    CONTROLLED=6
    TOPIC=7
    HELP=8
    SHOW=9
    COMMANDS=10
    LIST=11
    TOPICS=12
    INFO=13
    INT=14
    STRING=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generatePoem(self):
            return self.getTypedRuleContext(PoemDSLParser.GeneratePoemContext,0)


        def generateControlledPoem(self):
            return self.getTypedRuleContext(PoemDSLParser.GenerateControlledPoemContext,0)


        def helpCommand(self):
            return self.getTypedRuleContext(PoemDSLParser.HelpCommandContext,0)


        def listTopics(self):
            return self.getTypedRuleContext(PoemDSLParser.ListTopicsContext,0)


        def showModelInfo(self):
            return self.getTypedRuleContext(PoemDSLParser.ShowModelInfoContext,0)


        def getRuleIndex(self):
            return PoemDSLParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = PoemDSLParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.generatePoem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.generateControlledPoem()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.helpCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 15
                self.listTopics()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 16
                self.showModelInfo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneratePoemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GENERATE(self):
            return self.getToken(PoemDSLParser.GENERATE, 0)

        def POEM(self):
            return self.getToken(PoemDSLParser.POEM, 0)

        def MODEL(self):
            return self.getToken(PoemDSLParser.MODEL, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(PoemDSLParser.INT)
            else:
                return self.getToken(PoemDSLParser.INT, i)

        def CONTEXT(self):
            return self.getToken(PoemDSLParser.CONTEXT, 0)

        def STRING(self):
            return self.getToken(PoemDSLParser.STRING, 0)

        def STANZAS(self):
            return self.getToken(PoemDSLParser.STANZAS, 0)

        def getRuleIndex(self):
            return PoemDSLParser.RULE_generatePoem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneratePoem" ):
                listener.enterGeneratePoem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneratePoem" ):
                listener.exitGeneratePoem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneratePoem" ):
                return visitor.visitGeneratePoem(self)
            else:
                return visitor.visitChildren(self)




    def generatePoem(self):

        localctx = PoemDSLParser.GeneratePoemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_generatePoem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(PoemDSLParser.GENERATE)
            self.state = 20
            self.match(PoemDSLParser.POEM)
            self.state = 21
            self.match(PoemDSLParser.MODEL)
            self.state = 22
            self.match(PoemDSLParser.INT)
            self.state = 23
            self.match(PoemDSLParser.CONTEXT)
            self.state = 24
            self.match(PoemDSLParser.STRING)
            self.state = 25
            self.match(PoemDSLParser.STANZAS)
            self.state = 26
            self.match(PoemDSLParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenerateControlledPoemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GENERATE(self):
            return self.getToken(PoemDSLParser.GENERATE, 0)

        def CONTROLLED(self):
            return self.getToken(PoemDSLParser.CONTROLLED, 0)

        def POEM(self):
            return self.getToken(PoemDSLParser.POEM, 0)

        def CONTEXT(self):
            return self.getToken(PoemDSLParser.CONTEXT, 0)

        def STRING(self):
            return self.getToken(PoemDSLParser.STRING, 0)

        def TOPIC(self):
            return self.getToken(PoemDSLParser.TOPIC, 0)

        def INT(self):
            return self.getToken(PoemDSLParser.INT, 0)

        def getRuleIndex(self):
            return PoemDSLParser.RULE_generateControlledPoem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenerateControlledPoem" ):
                listener.enterGenerateControlledPoem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenerateControlledPoem" ):
                listener.exitGenerateControlledPoem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenerateControlledPoem" ):
                return visitor.visitGenerateControlledPoem(self)
            else:
                return visitor.visitChildren(self)




    def generateControlledPoem(self):

        localctx = PoemDSLParser.GenerateControlledPoemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_generateControlledPoem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(PoemDSLParser.GENERATE)
            self.state = 29
            self.match(PoemDSLParser.CONTROLLED)
            self.state = 30
            self.match(PoemDSLParser.POEM)
            self.state = 31
            self.match(PoemDSLParser.CONTEXT)
            self.state = 32
            self.match(PoemDSLParser.STRING)
            self.state = 33
            self.match(PoemDSLParser.TOPIC)
            self.state = 34
            self.match(PoemDSLParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HelpCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HELP(self):
            return self.getToken(PoemDSLParser.HELP, 0)

        def SHOW(self):
            return self.getToken(PoemDSLParser.SHOW, 0)

        def COMMANDS(self):
            return self.getToken(PoemDSLParser.COMMANDS, 0)

        def getRuleIndex(self):
            return PoemDSLParser.RULE_helpCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelpCommand" ):
                listener.enterHelpCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelpCommand" ):
                listener.exitHelpCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelpCommand" ):
                return visitor.visitHelpCommand(self)
            else:
                return visitor.visitChildren(self)




    def helpCommand(self):

        localctx = PoemDSLParser.HelpCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_helpCommand)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PoemDSLParser.HELP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(PoemDSLParser.HELP)
                pass
            elif token in [PoemDSLParser.SHOW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(PoemDSLParser.SHOW)
                self.state = 38
                self.match(PoemDSLParser.COMMANDS)
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


    class ListTopicsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(PoemDSLParser.LIST, 0)

        def TOPICS(self):
            return self.getToken(PoemDSLParser.TOPICS, 0)

        def SHOW(self):
            return self.getToken(PoemDSLParser.SHOW, 0)

        def getRuleIndex(self):
            return PoemDSLParser.RULE_listTopics

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListTopics" ):
                listener.enterListTopics(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListTopics" ):
                listener.exitListTopics(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListTopics" ):
                return visitor.visitListTopics(self)
            else:
                return visitor.visitChildren(self)




    def listTopics(self):

        localctx = PoemDSLParser.ListTopicsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listTopics)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PoemDSLParser.LIST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(PoemDSLParser.LIST)
                self.state = 42
                self.match(PoemDSLParser.TOPICS)
                pass
            elif token in [PoemDSLParser.SHOW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(PoemDSLParser.SHOW)
                self.state = 44
                self.match(PoemDSLParser.TOPICS)
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


    class ShowModelInfoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(PoemDSLParser.SHOW, 0)

        def MODEL(self):
            return self.getToken(PoemDSLParser.MODEL, 0)

        def INFO(self):
            return self.getToken(PoemDSLParser.INFO, 0)

        def getRuleIndex(self):
            return PoemDSLParser.RULE_showModelInfo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowModelInfo" ):
                listener.enterShowModelInfo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowModelInfo" ):
                listener.exitShowModelInfo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowModelInfo" ):
                return visitor.visitShowModelInfo(self)
            else:
                return visitor.visitChildren(self)




    def showModelInfo(self):

        localctx = PoemDSLParser.ShowModelInfoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_showModelInfo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(PoemDSLParser.SHOW)
            self.state = 48
            self.match(PoemDSLParser.MODEL)
            self.state = 49
            self.match(PoemDSLParser.INFO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





