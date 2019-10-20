from Classes import *

class IntermediateGenerator:
    def __init__(self):
        self.Quadruples = []
        self.stackOperators = []
        self.stackVariables = []
        self.counter = 1

    def addVar(self,variable:Operand):
        self.stackVariables.append(variable)

    def addOperator(self,operator:str):
        self.stackOperators.append(operator)

    def removeOperator(self):
        self.stackOperators.pop()

    def exitExp(self):
        pass

    def exitTermino(self):
        pass

    def exitFactor(self):
        pass
 
    def iniciaParentesis(self):
        pass


            #Obtener tipos de los operandos
            #Si si             generateQuad(op,opdo_izq,opdo_der)


    def finParentesis(self):
        # Aqui es donde va a quitar el fondo falso
        pass