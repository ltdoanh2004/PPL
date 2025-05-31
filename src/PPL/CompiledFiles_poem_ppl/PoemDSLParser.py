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
        4,1,10,28,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0,0,
        3,0,2,4,0,0,25,0,8,1,0,0,0,2,10,1,0,0,0,4,19,1,0,0,0,6,9,3,2,1,0,
        7,9,3,4,2,0,8,6,1,0,0,0,8,7,1,0,0,0,9,1,1,0,0,0,10,11,5,1,0,0,11,
        12,5,2,0,0,12,13,5,3,0,0,13,14,5,8,0,0,14,15,5,4,0,0,15,16,5,9,0,
        0,16,17,5,5,0,0,17,18,5,8,0,0,18,3,1,0,0,0,19,20,5,1,0,0,20,21,5,
        6,0,0,21,22,5,2,0,0,22,23,5,4,0,0,23,24,5,9,0,0,24,25,5,7,0,0,25,
        26,5,8,0,0,26,5,1,0,0,0,1,8
    ]

class PoemDSLParser ( Parser ):

    grammarFileName = "PoemDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'POEM'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'CONTROLLED'" ]

    symbolicNames = [ "<INVALID>", "GENERATE", "POEM", "MODEL", "CONTEXT", 
                      "STANZAS", "CONTROLLED", "TOPIC", "INT", "STRING", 
                      "WS" ]

    RULE_command = 0
    RULE_generatePoem = 1
    RULE_generateControlledPoem = 2

    ruleNames =  [ "command", "generatePoem", "generateControlledPoem" ]

    EOF = Token.EOF
    GENERATE=1
    POEM=2
    MODEL=3
    CONTEXT=4
    STANZAS=5
    CONTROLLED=6
    TOPIC=7
    INT=8
    STRING=9
    WS=10

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
            self.state = 8
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.generatePoem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.generateControlledPoem()
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
            self.state = 10
            self.match(PoemDSLParser.GENERATE)
            self.state = 11
            self.match(PoemDSLParser.POEM)
            self.state = 12
            self.match(PoemDSLParser.MODEL)
            self.state = 13
            self.match(PoemDSLParser.INT)
            self.state = 14
            self.match(PoemDSLParser.CONTEXT)
            self.state = 15
            self.match(PoemDSLParser.STRING)
            self.state = 16
            self.match(PoemDSLParser.STANZAS)
            self.state = 17
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
            self.state = 19
            self.match(PoemDSLParser.GENERATE)
            self.state = 20
            self.match(PoemDSLParser.CONTROLLED)
            self.state = 21
            self.match(PoemDSLParser.POEM)
            self.state = 22
            self.match(PoemDSLParser.CONTEXT)
            self.state = 23
            self.match(PoemDSLParser.STRING)
            self.state = 24
            self.match(PoemDSLParser.TOPIC)
            self.state = 25
            self.match(PoemDSLParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





