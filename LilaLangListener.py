from LilaParser import LilaParser
from LilaListener import LilaListener
from Classes import Semantic, Function, Var
from IntermediateGenerator import IntermediateGenerator

class LilaLangListener(LilaListener):

    # Enter a parse tree produced by LilaParser#programa.
    def enterPrograma(self, ctx:LilaParser.ProgramaContext):
        pass        
            
    # Exit a parse tree produced by LilaParser#programa.
    def exitPrograma(self, ctx:LilaParser.ProgramaContext):
        pass

    # Enter a parse tree produced by LilaParser#data.
    def enterData(self, ctx:LilaParser.DataContext):
        pass

    # Exit a parse tree produced by LilaParser#data.
    def exitData(self, ctx:LilaParser.DataContext):
        pass

    # Enter a parse tree produced by LilaParser#data2.
    def enterData2(self, ctx:LilaParser.Data2Context):
        i = 0
        while (ctx.ID(i) != None):
            varTemp = Var(str(ctx.ID(i)),ctx.tipo().getText(),'')
            if ( Semantic.add_var(varTemp) == False):
                # This means that the variable is already defined in the scope or globally
                raise SyntaxError("Variable " + str(ctx.ID(i)) + " is already declared in the actual scope")
            i = i+1

    # Exit a parse tree produced by LilaParser#data2.
    def exitData2(self, ctx:LilaParser.Data2Context):
        pass
    # Enter a parse tree produced by LilaParser#main.
    def enterMain(self, ctx:LilaParser.MainContext):
        pass
    # Exit a parse tree produced by LilaParser#main.
    def exitMain(self, ctx:LilaParser.MainContext):
        pass
    # Enter a parse tree produced by LilaParser#tipo.
    def enterTipo(self, ctx:LilaParser.TipoContext):
        pass
    
    # Exit a parse tree produced by LilaParser#tipo.
    def exitTipo(self, ctx:LilaParser.TipoContext):
        pass

    # Enter a parse tree produced by LilaParser#funciones.
    def enterFunciones(self, ctx:LilaParser.FuncionesContext):
        if(ctx.VOID() == None):
            #This is not a void function
            funcTemp = Function(str(ctx.ID()),ctx.tipo().getText())
        else:
            #This is a void function
            funcTemp = Function(str(ctx.ID()),ctx.VOID())

        if (Semantic.add_function(funcTemp) == False):
             # This means that the function is already defined in the program
            raise SyntaxError("Function " + str(ctx.ID()) + " is already defined")
        
        if ctx.params() != None:
            #Get all the IDs and Types for each parameter in a function
            (T,I) = self.enterParams(ctx.params())
            
            for a,b in zip(I,T):
                varTemp = Var(a.getText(),b.getText(),'')
                if ( Semantic.add_var(varTemp) == False):
                    # This means that the variable is already defined in the scope or globally
                    raise SyntaxError("Variable " + str(a.getText()) + " is already declared in the actual scope")
    # Exit a parse tree produced by LilaParser#funciones.
    def exitFunciones(self, ctx:LilaParser.FuncionesContext):
        pass    


    # Enter a parse tree produced by LilaParser#params.
    def enterParams(self, ctx:LilaParser.ParamsContext):
        return (ctx.tipo(),ctx.ID())

    # Exit a parse tree produced by LilaParser#params.
    def exitParams(self, ctx:LilaParser.ParamsContext):
        pass


    # Enter a parse tree produced by LilaParser#estatuto.
    def enterEstatuto(self, ctx:LilaParser.EstatutoContext):
        pass

    # Exit a parse tree produced by LilaParser#estatuto.
    def exitEstatuto(self, ctx:LilaParser.EstatutoContext):
        pass


    # Enter a parse tree produced by LilaParser#condicion.
    def enterCondicion(self, ctx:LilaParser.CondicionContext):
        pass

    # Exit a parse tree produced by LilaParser#condicion.
    def exitCondicion(self, ctx:LilaParser.CondicionContext):
        pass


    # Enter a parse tree produced by LilaParser#bloque.
    def enterBloque(self, ctx:LilaParser.BloqueContext):
        pass

    # Exit a parse tree produced by LilaParser#bloque.
    def exitBloque(self, ctx:LilaParser.BloqueContext):
        pass


    # Enter a parse tree produced by LilaParser#display.
    def enterDisplay(self, ctx:LilaParser.DisplayContext):
        pass

    # Exit a parse tree produced by LilaParser#display.
    def exitDisplay(self, ctx:LilaParser.DisplayContext):
        pass


    # Enter a parse tree produced by LilaParser#asignacion.
    def enterAsignacion(self, ctx:LilaParser.AsignacionContext):
        pass

    # Exit a parse tree produced by LilaParser#asignacion.
    def exitAsignacion(self, ctx:LilaParser.AsignacionContext):
        pass


    # Enter a parse tree produced by LilaParser#sreturn.
    def enterSreturn(self, ctx:LilaParser.SreturnContext):
        pass

    # Exit a parse tree produced by LilaParser#sreturn.
    def exitSreturn(self, ctx:LilaParser.SreturnContext):
        pass


    # Enter a parse tree produced by LilaParser#arr.
    def enterArr(self, ctx:LilaParser.ArrContext):
        pass

    # Exit a parse tree produced by LilaParser#arr.
    def exitArr(self, ctx:LilaParser.ArrContext):
        pass


    # Enter a parse tree produced by LilaParser#expresion.
    def enterExpresion(self, ctx:LilaParser.ExpresionContext):
        pass

    # Exit a parse tree produced by LilaParser#expresion.
    def exitExpresion(self, ctx:LilaParser.ExpresionContext):
        pass


    # Enter a parse tree produced by LilaParser#exp.
    def enterExp(self, ctx:LilaParser.ExpContext):
        pass

    # Exit a parse tree produced by LilaParser#exp.
    def exitExp(self, ctx:LilaParser.ExpContext):
        pass


    # Enter a parse tree produced by LilaParser#termino.
    def enterTermino(self, ctx:LilaParser.TerminoContext):
        pass

    # Exit a parse tree produced by LilaParser#termino.
    def exitTermino(self, ctx:LilaParser.TerminoContext):
        pass


    # Enter a parse tree produced by LilaParser#factor.
    def enterFactor(self, ctx:LilaParser.FactorContext):
        pass

    # Exit a parse tree produced by LilaParser#factor.
    def exitFactor(self, ctx:LilaParser.FactorContext):
        pass


    # Enter a parse tree produced by LilaParser#comparacion.
    def enterComparacion(self, ctx:LilaParser.ComparacionContext):
        pass

    # Exit a parse tree produced by LilaParser#comparacion.
    def exitComparacion(self, ctx:LilaParser.ComparacionContext):
        pass


    # Enter a parse tree produced by LilaParser#var_cte.
    def enterVar_cte(self, ctx:LilaParser.Var_cteContext):
        pass

    # Exit a parse tree produced by LilaParser#var_cte.
    def exitVar_cte(self, ctx:LilaParser.Var_cteContext):
        pass


    # Enter a parse tree produced by LilaParser#swhile.
    def enterSwhile(self, ctx:LilaParser.SwhileContext):
        pass

    # Exit a parse tree produced by LilaParser#swhile.
    def exitSwhile(self, ctx:LilaParser.SwhileContext):
        pass


    # Enter a parse tree produced by LilaParser#invocacion.
    def enterInvocacion(self, ctx:LilaParser.InvocacionContext):
        pass

    # Exit a parse tree produced by LilaParser#invocacion.
    def exitInvocacion(self, ctx:LilaParser.InvocacionContext):
        pass


    # Enter a parse tree produced by LilaParser#getinput.
    def enterGetinput(self, ctx:LilaParser.GetinputContext):
        pass

    # Exit a parse tree produced by LilaParser#getinput.
    def exitGetinput(self, ctx:LilaParser.GetinputContext):
        pass


    # Enter a parse tree produced by LilaParser#especiales.
    def enterEspeciales(self, ctx:LilaParser.EspecialesContext):
        pass

    # Exit a parse tree produced by LilaParser#especiales.
    def exitEspeciales(self, ctx:LilaParser.EspecialesContext):
        pass

