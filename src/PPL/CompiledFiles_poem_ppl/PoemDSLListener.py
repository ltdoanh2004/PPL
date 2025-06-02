# Generated from /Users/doa_ai/Developer/Poem_PPL/src/PPL/PoemDSL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PoemDSLParser import PoemDSLParser
else:
    from PoemDSLParser import PoemDSLParser

# This class defines a complete listener for a parse tree produced by PoemDSLParser.
class PoemDSLListener(ParseTreeListener):

    # Enter a parse tree produced by PoemDSLParser#command.
    def enterCommand(self, ctx:PoemDSLParser.CommandContext):
        pass

    # Exit a parse tree produced by PoemDSLParser#command.
    def exitCommand(self, ctx:PoemDSLParser.CommandContext):
        pass


    # Enter a parse tree produced by PoemDSLParser#generatePoem.
    def enterGeneratePoem(self, ctx:PoemDSLParser.GeneratePoemContext):
        pass

    # Exit a parse tree produced by PoemDSLParser#generatePoem.
    def exitGeneratePoem(self, ctx:PoemDSLParser.GeneratePoemContext):
        pass


    # Enter a parse tree produced by PoemDSLParser#generateControlledPoem.
    def enterGenerateControlledPoem(self, ctx:PoemDSLParser.GenerateControlledPoemContext):
        pass

    # Exit a parse tree produced by PoemDSLParser#generateControlledPoem.
    def exitGenerateControlledPoem(self, ctx:PoemDSLParser.GenerateControlledPoemContext):
        pass


    # Enter a parse tree produced by PoemDSLParser#helpCommand.
    def enterHelpCommand(self, ctx:PoemDSLParser.HelpCommandContext):
        pass

    # Exit a parse tree produced by PoemDSLParser#helpCommand.
    def exitHelpCommand(self, ctx:PoemDSLParser.HelpCommandContext):
        pass


    # Enter a parse tree produced by PoemDSLParser#listTopics.
    def enterListTopics(self, ctx:PoemDSLParser.ListTopicsContext):
        pass

    # Exit a parse tree produced by PoemDSLParser#listTopics.
    def exitListTopics(self, ctx:PoemDSLParser.ListTopicsContext):
        pass


    # Enter a parse tree produced by PoemDSLParser#showModelInfo.
    def enterShowModelInfo(self, ctx:PoemDSLParser.ShowModelInfoContext):
        pass

    # Exit a parse tree produced by PoemDSLParser#showModelInfo.
    def exitShowModelInfo(self, ctx:PoemDSLParser.ShowModelInfoContext):
        pass



del PoemDSLParser