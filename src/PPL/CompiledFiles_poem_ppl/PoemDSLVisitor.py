# Generated from /Users/doa_ai/Developer/Poem_PPL/src/PPL/PoemDSL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PoemDSLParser import PoemDSLParser
else:
    from PoemDSLParser import PoemDSLParser

# This class defines a complete generic visitor for a parse tree produced by PoemDSLParser.

class PoemDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PoemDSLParser#command.
    def visitCommand(self, ctx:PoemDSLParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoemDSLParser#generatePoem.
    def visitGeneratePoem(self, ctx:PoemDSLParser.GeneratePoemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoemDSLParser#generateControlledPoem.
    def visitGenerateControlledPoem(self, ctx:PoemDSLParser.GenerateControlledPoemContext):
        return self.visitChildren(ctx)



del PoemDSLParser