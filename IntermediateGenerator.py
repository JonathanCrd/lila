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

        self.params_reader = []

        # Counter for the temp and params name
        self.var_counter = 1
        self.param_counter = 1

        self.stack_dim = []

        self.cube = Semantic_Cube()

    def addVar(self,variable:Operand):
        self.stack_variables.append(variable)

    def addConst(self, constant:Operand):
        ##Search if the constant already exists
        if constant.value not in VirtualAddress.constants_table:
            VirtualAddress.constants_table[constant.value] = [constant.v_type, VirtualAddress.getAddress('Const ' + str(constant.v_type))]

        constant.memory = VirtualAddress.constants_table[constant.value][1]
        self.stack_variables.append(constant)

    def addFunct(self,function:Function):
        '''
        Tratar a la funcion como una variable para el caso de asignacion
        '''
        temp = Operand('t'+str(self.var_counter),function.f_type,None)
        temp.memory = VirtualAddress.getAddress('Temp '+str(temp.v_type))
        Semantic.Era.var_counters['Temp '+str(temp.v_type)] += 1
        self.Quadruples.append(Quadruple('=',Semantic.look_for_variable(function.name),None,temp))
        self.var_counter += 1
        self.addVar(temp)

    def addOperator(self,operator:str):
        '''
        Add operator to the stack
        '''
        self.stack_operators.append(operator)

    def top_operators(self):
        '''
        Return the top operator withouth pop it.
        '''
        if self.stack_operators == []:
            return None
        else:
            return self.stack_operators[-1]

    def top_variables(self):
        '''
        Return the top variable withouth pop it.
        '''
        if self.stack_variables == []:
            return None
        else:
            return self.stack_variables[-1]
    
    def display(self):
        '''
        Generates the display quadruple
        '''
        opnd = self.stack_variables.pop()
        self.Quadruples.append(Quadruple('DISPLAY',None,None,opnd))
    
    def getinput(self,variable:Operand,message):
        '''
        Generates INPUT cuadruple.
        '''
        variable.value = message
        self.Quadruples.append(Quadruple('INPUT',None,None,variable))

    def func_return(self):
        '''
        Generates the RETURN quadruple with the operand to assign to an specific function.
        '''
        opnd = self.stack_variables.pop()
        func = Semantic.varGlobals[Semantic.lastFuncKey].memory
        self.Quadruples.append(Quadruple('RETURN',opnd,None,func))
    
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
        '''
        Creates a new ERA object for the main block
        '''
        Semantic.Era = ERA()
        self.var_counter = 1

    def exitExpresion(self):
        '''
        Genera el cuadruplo con el operador y los operandos en las pilas.
        '''
        if self.top_operators() == 'AND' or self.top_operators() == 'OR':
            op = self.stack_operators.pop()
            opnd_Der = self.stack_variables.pop()
            opnd_Izq = self.stack_variables.pop()
            #Checa los tipos de los operandos, si son compatibles, genera cuadruplo
            if(Semantic_Cube.cube[str(opnd_Izq.v_type)][str(opnd_Der.v_type)][str(op)] != None):
                # Resultado se agrega a la pila de variables
                res = Operand('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
                res.memory = VirtualAddress.getAddress('Temp '+str(res.v_type))
                Semantic.Era.var_counters['Temp '+str(res.v_type)] += 1
                ##Hay que hacer validacion de si se pudo?
                self.var_counter += 1
                self.stack_variables.append(res)
                # Genera cuadruplo
                self.Quadruples.append(Quadruple(op,opnd_Izq,opnd_Der,res))
            else:
                raise TypeError('Variable of type "' + str(opnd_Izq.v_type) + '" is not compatible with type "'+ str(opnd_Der.v_type +'" using "'+str(op))+'"')
            
    def exitComparacion(self):
        '''
        Generates the quadruple with the operator in the stack.
        '''
        if self.top_operators() == '>' or self.top_operators() == '<' or self.top_operators() == '!=' or self.top_operators() == '==' or self.top_operators() == '>=' or self.top_operators() == '<=':
            op = self.stack_operators.pop()
            opnd_Der = self.stack_variables.pop()
            opnd_Izq = self.stack_variables.pop()
            #Checa los tipos de los operandos, si son compatibles, genera cuadruplo
            if(Semantic_Cube.cube[str(opnd_Izq.v_type)][str(opnd_Der.v_type)][str(op)] != None):
                # Resultado se agrega a la pila de variables
                res = Operand('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
                res.memory = VirtualAddress.getAddress('Temp '+str(res.v_type))
                Semantic.Era.var_counters['Temp '+str(res.v_type)] += 1
                self.var_counter += 1
                self.stack_variables.append(res)
                # Genera cuadruplo
                self.Quadruples.append(Quadruple(op,opnd_Izq,opnd_Der,res))
            else:
                raise TypeError('Variable of type "' + str(opnd_Izq.v_type) + '" is not compatible with type "'+ str(opnd_Der.v_type +'" using "'+str(op))+'"')

    def exitExp(self):
        '''
        Generates the arithmetic quadruple.
        '''
        if self.top_operators() == '+' or self.top_operators() == '-':
            op = self.stack_operators.pop()
            opnd_Der = self.stack_variables.pop()
            opnd_Izq = self.stack_variables.pop()
            #Checa los tipos de los operandos, si son compatibles, genera cuadruplo
            if(Semantic_Cube.cube[str(opnd_Izq.v_type)][str(opnd_Der.v_type)][str(op)] != None):
                # Resultado se agrega a la pila de variables
                res = Operand('t'+str(self.var_counter),Semantic_Cube.cube[opnd_Izq.v_type][opnd_Der.v_type][op],None)
                res.memory = VirtualAddress.getAddress('Temp '+str(res.v_type))
                Semantic.Era.var_counters['Temp '+str(res.v_type)] += 1
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
                res.memory = VirtualAddress.getAddress('Temp '+str(res.v_type))
                Semantic.Era.var_counters['Temp '+str(res.v_type)] += 1
                self.var_counter += 1
                self.stack_variables.append(res)
                # Genera cuadruplo
                self.Quadruples.append(Quadruple(op,opnd_Izq,opnd_Der,res))
            else:
                raise TypeError('Variable of type "' + str(opnd_Izq.v_type) + '" is not compatible with type "'+ str(opnd_Der.v_type +'" using "'+str(op))+'"')

    def finParentesis(self):
        '''
        Pop of ).
        '''
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
        '''
        Fills the last pending jump in the jumps stacks.
        Usefull when the condition ends or when the main block is found.
        '''
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
        #Semantic.dirFunctions[funct_name].memory_required)
        self.Quadruples.append(Quadruple("ERA",None,None, funct_name))

    def params(self):
        var_temp = self.stack_variables.pop()
        self.params_reader[-1].append(var_temp)
        self.Quadruples.append(Quadruple('PARAM',var_temp,None,Operand('param' + str(self.param_counter),None,None)))
        self.param_counter += 1
        
    def check_params(self, funct_name):
        '''
        Method that verifies each param and that the number of params in the call math the function declaration.
        '''
        params_declared = Semantic.dirFunctions[funct_name].params
        params_found = self.params_reader[-1]
        if(len(params_found) == len(params_declared)):
            for i in range(0,len(params_found)):
                if(params_found[i].v_type != params_declared[i].v_type):
                    raise TypeError("Param '" + params_found[i].name + "' should be of type " + params_declared[i].v_type)
        else:
            raise SyntaxError("Function '"+ funct_name + "' expects " + str(len(params_declared)) + " params, but instead got " + str(len(params_found)))

        self.params_reader.pop()

    def incoming_Params(self):
        '''
        Apend a blank list to the params reader.
        '''
        self.params_reader.append([])

    def endProc(self):
        '''
        Generates ENDPROC and reset locals.
        '''
        VirtualAddress.resetLocals()
        self.Quadruples.append(Quadruple('ENDPROC',None,None,None))

    def end(self):
        '''
        Generates the quadruple END and adds the 'main' block to the function directory.
        '''
        main = Function('main', 'void', None) #The quadruple index is irrelevant for the main block in the dir_function
        main.memory_required = Semantic.Era.var_counters
        Semantic.add_function(main)
        self.Quadruples.append(Quadruple('END',None,None,None))

    def getObj(self):
        '''
        Returns the OBJ in form of a dictionary needed for the virtual machine.
        '''
        return {'quadruples': self.Quadruples, 'constant_table': VirtualAddress.constants_table, 'dir_functions': Semantic.dirFunctions, 'memory_declaration': VirtualAddress.memory_declaration} 
        
    def makeNegative(self,minus):
        if (minus == '-'):
            exp = self.stack_variables.pop()
            if(exp.v_type=='int'):
                pass
            elif (exp.v_type=='num'):
                pass
            else:
                raise TypeError("Variable "+str(exp.v_type)+" can't be negative")
            
            res = Operand('t'+str(self.var_counter),exp.v_type,None)
            res.memory = VirtualAddress.getAddress('Temp '+str(res.v_type))
            Semantic.Era.var_counters['Temp '+str(res.v_type)] += 1
            self.var_counter += 1
            self.stack_variables.append(res)
            self.Quadruples.append(Quadruple('NEGATIVE',exp,-1,res))

    def access_array_begin(self):
        '''
        This method is going to append a 0 to the stack dimension.
        '''
        var = self.stack_variables.pop()
        Semantic.check_var_dim(var.name)
        self.stack_dim.append(0)
        Semantic.total_dims.append(0)

    def VER(self, v_id):
        '''
        Generates the VER quadruple
        '''
        Semantic.count_dim(v_id)
        Semantic.checkMoreDims(v_id)

        t_var = self.stack_variables[-1]
        dim_var = Semantic.look_for_variable(v_id)
        dim_struct = dim_var.array[self.stack_dim[-1]]
        self.Quadruples.append(Quadruple('VER',t_var,0, dim_struct.upper_limit))

        if (dim_struct.m != 1):
            aux = self.stack_variables.pop()
            temp = Operand('t'+str(self.var_counter),'int',None)
            temp.memory = VirtualAddress.getAddress('Temp '+str(temp.v_type))
            self.var_counter += 1
            m = Operand('m','int',dim_struct.m)
            m.memory = VirtualAddress.constants_table[str(int(dim_struct.m))][1]
            self.Quadruples.append(Quadruple('*', aux, m, temp))
            self.stack_variables.append(temp)
        
        if (self.stack_dim[-1] > 0):
            aux2 = self.stack_variables.pop()
            aux1 = self.stack_variables.pop()
            temp = Operand('t'+str(self.var_counter),'int',None)
            temp.memory = VirtualAddress.getAddress('Temp '+str(temp.v_type))
            self.var_counter += 1
            self.Quadruples.append(Quadruple('+',aux1,aux2,temp))
            self.stack_variables.append(temp)

        self.stack_dim[-1] += 1

    def access_array_end(self,v_id):
        '''
        This method is going to pop the last item of the stack dimension.
        '''
        aux = self.stack_variables.pop()
        v_type = Semantic.look_for_variable(v_id)
        temp = Operand('t'+str(self.var_counter),v_type.v_type,None)
        temp.memory = VirtualAddress.getAddress('Temp '+str(temp.v_type))
        temp.pointer = True
        self.Quadruples.append(Quadruple('+BASE',aux, Semantic.look_for_variable(v_id), temp))
        self.stack_variables.append(temp)
        self.stack_dim.pop()
    
    def q_basics(self,param_name:str,Operator:str):
        self.Quadruples.append(Quadruple(Operator, None, None, None))
        param = Semantic.look_for_variable(param_name)
        self.Quadruples.append(Quadruple('ARR',param.memory,param.array[0].upper_limit,param.v_type))
    
    def q_twoParams(self,param_name:str,Operator:str):
        '''
        get the last 2 variables of the stack and generates 2 ARR quadruple instead of just one.
        '''
        varB = self.stack_variables.pop()
        varA = self.stack_variables.pop()

        if varA.array[0].upper_limit != varB.array[0].upper_limit:
            raise IndexError("This function expects arrays of the same size")
        else:
            self.Quadruples.append(Quadruple(Operator, None, None, None))
            self.Quadruples.append(Quadruple('ARR',varA.memory,varA.array[0].upper_limit,varA.v_type))
            self.Quadruples.append(Quadruple('ARR',varB.memory,varB.array[0].upper_limit,varB.v_type))

    def q_fill_value(self,param_name:str,Operator:str):
        '''
        Generates fill quadruple for fill value function.
        '''
        replacement = self.stack_variables.pop()
        varToReplace = self.stack_variables.pop()
        param = Semantic.look_for_variable(param_name)

        if(replacement.v_type == varToReplace.v_type and varToReplace.v_type == param.v_type):
            self.Quadruples.append(Quadruple(Operator, varToReplace, replacement, None))
            self.Quadruples.append(Quadruple('ARR',param.memory,param.array[0].upper_limit,None))
        else:
            raise TypeError("All parameters should be of the same type")

    def q_remove_value(self,param_name:str,Operator:str):
        varToRemove = self.stack_variables.pop()
        param = Semantic.look_for_variable(param_name)

        if(varToRemove.v_type == param.v_type):
            self.Quadruples.append(Quadruple(Operator, varToRemove, None, None))
            self.Quadruples.append(Quadruple('ARR',param.memory,param.array[0].upper_limit,None))
        else:
            raise TypeError("All parameters should be of the same type")
        

    def test_final(self):
        pass
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
                        try:
                            print(i,'[',item.operator,'(',item.left.name, item.left.v_type, item.left.value,item.left.memory,')',item.right,item.resultado,"]")
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
#
        print("DIR DE FUNCIONES")
        for x,y in Semantic.dirFunctions.items():
            print(x, y.name, y.f_type, len(y.params), y.memory_required)
        