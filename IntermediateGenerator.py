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
        self.stack_jumps = []
        self.counter = 1
        self.var_counter = 1
        self.param_counter = 1
        self.cube = Semantic_Cube()

    def addVar(self,variable:Operand):
        self.stack_variables.append(variable)

    def addConst(self, constant:Operand):
        ##Search if the constant already exists
        if constant.value not in VirtualAddress.constants_table:
            VirtualAddress.constants_table[constant.value] = VirtualAddress.getAddress('Const ' + str(constant.v_type))
        
        constant.memory = VirtualAddress.constants_table[constant.value]
        self.stack_variables.append(constant)

    '''
    Tratar a la funcion como una variable para el caso de asignacion
    '''
    def addFunct(self,function:Function):
        temp = Operand('t'+str(self.var_counter),function.f_type,None)
        temp.memory = VirtualAddress.getAddress('Global '+str(temp.v_type))
        self.Quadruples.append(Quadruple('=',function.name,None,temp))
        self.var_counter += 1
        self.addVar(temp)

    def addOperator(self,operator:str):
        self.stack_operators.append(operator)

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
    
    def display(self):
        opnd = self.stack_variables.pop()
        self.Quadruples.append(Quadruple('DISPLAY',None,None,opnd))
    
    def getinput(self,variable:Operand):
        self.Quadruples.append(Quadruple('INPUT',None,None,variable))

    def func_return(self):
        opnd = self.stack_variables.pop()

        self.Quadruples.append(Quadruple('RETURN',None,None,opnd))
    
    def assign(self):
        if self.top_operators() == '=':
            op = self.stack_operators.pop()
            opnd_Der = self.stack_variables.pop()
            opnd_Izq = self.stack_variables.pop()
            #Checa los tipos de los operandos, si son compatibles, genera cuadruplo
            if(Semantic_Cube.cube[str(opnd_Izq.v_type)][str(opnd_Der.v_type)][str(op)] != None):
                # Genera cuadruplo
                self.Quadruples.append(Quadruple(op,opnd_Der,None,opnd_Izq))
            else:
                raise TypeError('Variable of type "' + str(opnd_Izq.v_type) + '" is not compatible with type "'+ str(opnd_Der.v_type +'" using "'+str(op))+'"') 

    def contextChange(self):
        self.var_counter = 1

    def exitExpresion(self):
        if self.top_operators() == 'AND' or self.top_operators() == 'OR':
            op = self.stack_operators.pop()
            opnd_Der = self.stack_variables.pop()
            opnd_Izq = self.stack_variables.pop()
            #Checa los tipos de los operandos, si son compatibles, genera cuadruplo
            if(Semantic_Cube.cube[str(opnd_Izq.v_type)][str(opnd_Der.v_type)][str(op)] != None):
                # Resultado se agrega a la pila de variables
                res = Operand('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
                
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
                res = Operand('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
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
                res = Operand('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
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
                res = Operand('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
                self.var_counter += 1
                self.stack_variables.append(res)
                # Genera cuadruplo
                self.Quadruples.append(Quadruple(op,opnd_Izq,opnd_Der,res))
            else:
                raise TypeError('Variable of type "' + str(opnd_Izq.v_type) + '" is not compatible with type "'+ str(opnd_Der.v_type +'" using "'+str(op))+'"')

    def finParentesis(self):
        # Aqui es donde va a quitar el fondo falso
        if self.top_operators() == '(':
            self.stack_operators.pop()
        else:
            raise SyntaxError("Parenthesis ( not found")
    
    def checkExpresion(self):
        res = self.stack_variables.pop()
        if(res.v_type != 'bool'):
            raise TypeError("Condition is not boolean")
        else:
            self.Quadruples.append(Quadruple("GOTOF",res,None,None))
            self.stack_jumps.append(len(self.Quadruples)-1)
    
    def conditionEnd(self):
        end = self.stack_jumps.pop()
        self.fill(end,len(self.Quadruples))

    #X es el cuadruplo a rellenar, y cont es el valor de relleno
    def fill(self,x,cont):
        self.Quadruples[x].resultado = Operand(None,None,cont+1)
        #print(self.Quadruples[x].operator,self.Quadruples[x].left,self.Quadruples[x].right,self.Quadruples[x].resultado)

    def conditionElse(self):
        self.Quadruples.append(Quadruple("GOTO",None,None,None))
        false = self.stack_jumps.pop()
        self.stack_jumps.append(len(self.Quadruples)-1)
        self.fill(false,len(self.Quadruples))

    def swhile(self):
        self.stack_jumps.append(len(self.Quadruples))

    def whileEnd(self):
        end = self.stack_jumps.pop()
        sreturn = self.stack_jumps.pop()
        self.Quadruples.append(Quadruple("GOTO",None,None,Operand(None,None,sreturn+1)))
        self.fill(end,len(self.Quadruples))

    def goTo(self):
        self.Quadruples.append(Quadruple("GOTO",None,None,None))
        self.stack_jumps.append(len(self.Quadruples)-1)
        
    def goSub(self,funct_name):
        index = Semantic.dirFunctions[funct_name].quadruple_index
        self.Quadruples.append(Quadruple("GOSUB",None,None,Operand(funct_name,None,index+1)))
        
    def era(self,funct_name):
        self.Quadruples.append(Quadruple("ERA",None,None,Operand(funct_name,None,None)))

    def params(self):
        var_temp = self.stack_variables.pop()
        self.Quadruples.append(Quadruple('param',Operand(var_temp.name,var_temp.v_type,var_temp.value),None,Operand('param' + str(self.param_counter),None,None)))

    def endProc(self):
        self.Quadruples.append(Quadruple('ENDPROC',None,None,None))

    def end(self):
        self.Quadruples.append(Quadruple('end',None,None,None))

    def test_final(self):
        i=1
        print("Quadruples length: ",len(self.Quadruples))
        print('=======')
        for item in self.Quadruples:
           try:
               print(i,'[',item.operator,'(',item.left.name, item.left.v_type, item.left.value, item.left.memory,')','(',item.right.name, item.right.v_type, item.right.value,item.right.memory,')','(',item.resultado.name,item.resultado.v_type,item.resultado.value,item.resultado.memory,")]")
               i+=1
           except:
                try:
                    print(i,'[',item.operator,'(',item.left.name, item.left.v_type, item.left.value,item.left.memory,')',item.right,'(',item.resultado.name,item.resultado.v_type,item.resultado.value,item.resultado.memory,")]")
                    i+=1
                except:
                    try:
                        print(i,'[',item.operator,item.left,item.right,'(',item.resultado.name,item.resultado.v_type,item.resultado.value,item.resultado.memory,")]")
                        i+=1
                    except:
                        print(i,'[',item.operator,item.left,item.right,item.resultado,']')
                        i+=1
        print('=======')
        
        print("STACK DE VARIABLES")
        for variable in self.stack_variables:
            print(str(variable.name) + " " + str(variable.v_type) + " " + str(variable.value) )

        print("TABLA DE CONSTANTES")
        print(VirtualAddress.constants_table)