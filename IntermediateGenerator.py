from Classes import *

class Quadruple:
    def __init__(self, operator, left, right,resultado):
        self.operator = operator
        self.left = left
        self.right = right
        self.resultado = resultado
        
class IntermediateGenerator:
    def __init__(self):
        self.Quadruples = []
        self.stack_operators = []
        self.stack_variables = []
        self.counter = 1
        self.var_counter = 1
        self.cube = Semantic_Cube()

    def addVar(self,variable:Var):
        self.stack_variables.append(variable)

    def addOperator(self,operator:str):
        self.stack_operators.append(operator)

    def removeOperator(self):
        if(self.stack_operators != []):
            self.stack_operators.pop()

    def top_operators(self):
        if self.stack_operators == []:
            return None
        else:
            return self.stack_operators[-1]

    def top_variables(self):
        if self.stack_variables == []:
            return None
        else:
            return self.stack_variables[-1]

    def exitExpresion(self):
        if self.top_operators() == 'AND' or self.top_operators() == 'OR':
            op = self.stack_operators.pop()
            opnd_Der = self.stack_variables.pop()
            opnd_Izq = self.stack_variables.pop()
            #Checa los tipos de los operandos, si son compatibles, genera cuadruplo
            if(Semantic_Cube.cube[str(opnd_Izq.v_type)][str(opnd_Der.v_type)][str(op)] != None):
                # Resultado se agrega a la pila de variables
                res = Var('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
                self.var_counter += 1
                self.stack_variables.append(res)
                # Genera cuadruplo
                self.Quadruples.append(Quadruple(op,opnd_Izq,opnd_Der,res))
            else:
                raise TypeError('Variable of type "' + str(opnd_Izq.v_type) + '" is not compatible with type "'+ str(opnd_Der.v_type +'" using "'+str(op))+'"')
            
    def exitComparacion(self):
        if self.top_operators() == '>' or self.top_operators() == '<' or self.top_operators() == '!=' or self.top_operators() == '==' or self.top_operators() == '>=' or self.top_operators() == '<=':
            op = self.stack_operators.pop()
            opnd_Der = self.stack_variables.pop()
            opnd_Izq = self.stack_variables.pop()
            #Checa los tipos de los operandos, si son compatibles, genera cuadruplo
            if(Semantic_Cube.cube[str(opnd_Izq.v_type)][str(opnd_Der.v_type)][str(op)] != None):
                # Resultado se agrega a la pila de variables
                res = Var('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
                self.var_counter += 1
                self.stack_variables.append(res)
                # Genera cuadruplo
                self.Quadruples.append(Quadruple(op,opnd_Izq,opnd_Der,res))
            else:
                raise TypeError('Variable of type "' + str(opnd_Izq.v_type) + '" is not compatible with type "'+ str(opnd_Der.v_type +'" using "'+str(op))+'"')

    def exitExp(self):
        if self.top_operators() == '+' or self.top_operators() == '-':
            op = self.stack_operators.pop()
            opnd_Der = self.stack_variables.pop()
            opnd_Izq = self.stack_variables.pop()
            #Checa los tipos de los operandos, si son compatibles, genera cuadruplo
            if(Semantic_Cube.cube[str(opnd_Izq.v_type)][str(opnd_Der.v_type)][str(op)] != None):
                # Resultado se agrega a la pila de variables
                res = Var('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
                self.var_counter += 1
                self.stack_variables.append(res)
                # Genera cuadruplo
                self.Quadruples.append(Quadruple(op,opnd_Izq,opnd_Der,res))
            else:
                raise TypeError('Variable of type "' + str(opnd_Izq.v_type) + '" is not compatible with type "'+ str(opnd_Der.v_type +'" using "'+str(op))+'"')

    def exitTermino(self):
        if self.top_operators() == '*' or self.top_operators() == '/':
            op = self.stack_operators.pop()
            opnd_Der = self.stack_variables.pop()
            opnd_Izq = self.stack_variables.pop()
            #Checa los tipos de los operandos, si son compatibles, genera cuadruplo
            if(Semantic_Cube.cube[str(opnd_Izq.v_type)][str(opnd_Der.v_type)][str(op)] != None):
                # Resultado se agrega a la pila de variables
                res = Var('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
                self.var_counter += 1
                self.stack_variables.append(res)
                # Genera cuadruplo
                self.Quadruples.append(Quadruple(op,opnd_Izq,opnd_Der,res))
            else:
                raise TypeError('Variable of type "' + str(opnd_Izq.v_type) + '" is not compatible with type "'+ str(opnd_Der.v_type +'" using "'+str(op))+'"')
 
    def iniciaParentesis(self):
        self.stack_operators.append('(')

    def finParentesis(self):
        # Aqui es donde va a quitar el fondo falso
        if self.top_operators() == '(':
            self.stack_operators.pop()
        else:
            raise SyntaxError("Parenthesis ( not found")

    def test_final(self):
        print('=======')
        for item in self.Quadruples:
            print('[',item.operator,'(',item.left.name, item.left.v_type, item.left.value,')','(',item.right.name, item.right.v_type, item.right.value,')','(',item.resultado.name,item.resultado.v_type,item.resultado.value,")]")
        print('=======')