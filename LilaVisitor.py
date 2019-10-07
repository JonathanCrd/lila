# Generated from Lila.li by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LilaParser import LilaParser
else:
    from LilaParser import LilaParser

# This class defines a complete generic visitor for a parse tree produced by LilaParser.

class LilaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LilaParser#programa.
    def visitPrograma(self, ctx:LilaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#data.
    def visitData(self, ctx:LilaParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#main.
    def visitMain(self, ctx:LilaParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#tipo.
    def visitTipo(self, ctx:LilaParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#funciones.
    def visitFunciones(self, ctx:LilaParser.FuncionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#params.
    def visitParams(self, ctx:LilaParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#estatuto.
    def visitEstatuto(self, ctx:LilaParser.EstatutoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#condicion.
    def visitCondicion(self, ctx:LilaParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#bloque.
    def visitBloque(self, ctx:LilaParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#display.
    def visitDisplay(self, ctx:LilaParser.DisplayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#asignacion.
    def visitAsignacion(self, ctx:LilaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#sreturn.
    def visitSreturn(self, ctx:LilaParser.SreturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#arr.
    def visitArr(self, ctx:LilaParser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#expresion.
    def visitExpresion(self, ctx:LilaParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#exp.
    def visitExp(self, ctx:LilaParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#termino.
    def visitTermino(self, ctx:LilaParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#factor.
    def visitFactor(self, ctx:LilaParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#comparacion.
    def visitComparacion(self, ctx:LilaParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#var_cte.
    def visitVar_cte(self, ctx:LilaParser.Var_cteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#swhile.
    def visitSwhile(self, ctx:LilaParser.SwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#invocacion.
    def visitInvocacion(self, ctx:LilaParser.InvocacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#getinput.
    def visitGetinput(self, ctx:LilaParser.GetinputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LilaParser#especiales.
    def visitEspeciales(self, ctx:LilaParser.EspecialesContext):
        return self.visitChildren(ctx)



del LilaParser