class Function:
    def __init__(self, name, f_type, index):
        self.name = name
        self.f_type = f_type
        self.quadruple_index = index
        self.params = []

class Operand:
    def __init__(self, name, v_type, value):
        self.name = name
        self.v_type = v_type
        self.value = value
        self.memory = None

class VirtualAddress:
    segment_size = 2000
    memory_declaration = {
        'Global int'    : 5000, #4000
        'Global num'    : 6000,
        'Global text'   : 8000,
        'Global bool'   : 10000,
        'Local int'     : 9000, #20000
        'Local num'     : 22000,
        'Local text'    : 24000,
        'Local bool'    : 26000,
        'Temp int'      : 43000, #30000
        'Temp num'      : 32000,
        'Temp text'     : 34000,
        'Temp bool'     : 45000, #36000
        'Const int'     : 20000, #40000
        'Const num'     : 42000,
        'Const text'    : 44000,
        'Const bool'    : 48000
    }
    counters = {
        'Global int'    : 0,
        'Global num'    : 0,
        'Global text'   : 0,
        'Global bool'   : 0,
        'Local int'     : 0,
        'Local num'     : 0,
        'Local text'    : 0,
        'Local bool'    : 0,
        'Temp int'      : 0,
        'Temp num'      : 0,
        'Temp text'     : 0,
        'Temp bool'     : 0,
        'Const int'     : 0,
        'Const num'     : 0,
        'Const text'    : 0,
        'Const bool'    : 0
    }
    constants_table = {}

    @staticmethod
    def getAddress(a_type):
        tempAdress = VirtualAddress.memory_declaration[a_type] + VirtualAddress.counters[a_type]
        VirtualAddress.counters[a_type] += 1
        return tempAdress
    
    @staticmethod
    def resetLocals():
        VirtualAddress.counters['Local int'] = 0
        VirtualAddress.counters['Local num'] = 0
        VirtualAddress.counters['Local text'] = 0
        VirtualAddress.counters['Local bool'] = 0

class Semantic:
    dirFunctions = dict()
    varGlobals = dict()
    varFunct = dict()
    isGlobal = True
    lastFuncKey = None

    @staticmethod
    def enterFunciones(name,tipo,void,index):
        if(void == None):
           funcTemp = Function(name,tipo,index)
        else:
           funcTemp = Function(name,void,index)
     
        if (Semantic.add_function(funcTemp) == False):
             # This means that the function is already defined in the program
            raise SyntaxError("Function " + name + " is already defined")
            

    @staticmethod
    def add_function(function):
        '''
        Method to add a function into the function directory.
        It recieves an object Function to append, 
        if the function already exists, it will return false.
        '''
            
        if function.name not in Semantic.dirFunctions.keys():
            Semantic.dirFunctions[function.name] = function
            Semantic.lastFuncKey = function.name
           
            return True
        else:
            return False

    @staticmethod
    def add_var(var):
        '''
        Method to add a variable into the current scope table.
        It recieves an object Variable to append, 
        '''
        if Semantic.isGlobal == True:
            #This is a global variable
            if var.name not in Semantic.varGlobals:
                #Asociar direccion virtual 
                var.memory = VirtualAddress.getAddress('Global '+ str(var.v_type))
                Semantic.varGlobals[var.name] = var
            else:
                raise SyntaxError("Variable " + var.name  + " is already declared in the global scope")
        else:
            #This variable is inside an scope (It's a local variable)
            if var.name not in Semantic.varGlobals and var.name not in Semantic.varFunct:
                var.memory = VirtualAddress.getAddress('Local '+ str(var.v_type))
                Semantic.varFunct[var.name] = var
            else:
                raise SyntaxError("Variable " + var.name  + " is already declared in the actual scope")

    @staticmethod
    def add_param(var):
        '''
        Method to add a param into the current scope table.
        It recieves an object Variable to append, and also add 1 to the number of params in the current function
        '''
        if var.name not in Semantic.varGlobals and var.name not in Semantic.varFunct:
            var.memory = VirtualAddress.getAddress('Local '+ str(var.v_type))
            Semantic.varFunct[var.name] = var
            Semantic.dirFunctions[Semantic.lastFuncKey].params.append(var)
        else:
            raise SyntaxError("Variable " + var.name  + " is already declared in the actual scope")
    
    @staticmethod
    def dump_varFunt():
        '''
        Method to dump the variables of a function when 
        function is no longer needed.
        '''
        Semantic.varFunct = {}
    
    @staticmethod
    def look_for_function(function_name:str):
        #validate that the function exists
        if function_name in Semantic.dirFunctions.keys():
            return Semantic.dirFunctions[function_name]
        else:
            raise SyntaxError("Function '" + function_name  + "' is not declared.")

    @staticmethod
    def look_for_variable(var_name:str):
        if var_name in Semantic.varGlobals.keys():
            return Semantic.varGlobals[var_name]
        else:
            if var_name in Semantic.varFunct.keys():
                return Semantic.varFunct[var_name]
            else:
                raise SyntaxError("Variable '" + var_name  + "' is not declared.")

    @staticmethod
    def checkReturn(last_type):
        func_type = Semantic.dirFunctions[Semantic.lastFuncKey].f_type
        if func_type == 'void':
            raise SyntaxError("Function of type '"+ func_type + "' can't have a return")
        if func_type != last_type.v_type:
            raise SyntaxError("Function of type '"+ func_type + "' must return same type, can't return '" + last_type.v_type +"'")

    '''
    Check if the  function is void and depending on it expected value will raise an exception.
    Expected True means that the function is espected to be void.
    != void y quiera void -> invocacion OR  != void y no quiera void -> asignacion OR 
    '''
    @staticmethod
    def isVoid(funct_name:str,expected:bool):
        f_type = Semantic.dirFunctions[funct_name].f_type
        if f_type != 'void' and expected:
            raise SyntaxError("Function '" + funct_name + "' must be assigned to a variable since it is not void")
        else:
            if f_type == 'void' and not(expected):
                raise SyntaxError("Function '" + funct_name + "' cannot be used as operand since it is void")
    

    @staticmethod
    def display_test():
        # print("=============================")
        # print("DIR FUNCIONES: ")
        # for x, y in Semantic.dirFunctions.items():
        #     print(x, y.name, y.f_type, len(y.params))
        # print("\nVARS GLOBALESs: ")
        # for x, y in Semantic.varGlobals.items():
        #     print(x, y.name, y.v_type, y.value)
        # print("\nVARS LOCALES: ")
        # for x, y in Semantic.varFunct.items():
        #     print(x, y.name, y.v_type, y.value)
        # print("=============================")
        pass

class Semantic_Cube():
    cube = {}

    def __init__(self):
        # All types supported in Lila language
        types = ('int','num','text','bool')

        # Prepare the cube with the desire dimensions (3)
        for element in types:
            Semantic_Cube.cube[element] = {}
            for inner_element in types:
                Semantic_Cube.cube[element][inner_element] = {}

        # Set the result of each combination of types and operator in the cube
        Semantic_Cube.cube['int']['int']['+']='int'
        Semantic_Cube.cube['int']['int']['-']='int'
        Semantic_Cube.cube['int']['int']['/']='int'
        Semantic_Cube.cube['int']['int']['*']='int'
        Semantic_Cube.cube['int']['int']['>']='bool'
        Semantic_Cube.cube['int']['int']['<']='bool'
        Semantic_Cube.cube['int']['int']['>=']='bool'
        Semantic_Cube.cube['int']['int']['<=']='bool'
        Semantic_Cube.cube['int']['int']['==']='bool'
        Semantic_Cube.cube['int']['int']['!=']='bool'
        Semantic_Cube.cube['int']['int']['=']='int'
        Semantic_Cube.cube['int']['int']['AND']=None
        Semantic_Cube.cube['int']['int']['OR']=None
        Semantic_Cube.cube['int']['num']['+']='num'
        Semantic_Cube.cube['int']['num']['-']='num'
        Semantic_Cube.cube['int']['num']['/']='num'
        Semantic_Cube.cube['int']['num']['*']='num'
        Semantic_Cube.cube['int']['num']['>']='bool'
        Semantic_Cube.cube['int']['num']['<']='bool'
        Semantic_Cube.cube['int']['num']['>=']='bool'
        Semantic_Cube.cube['int']['num']['<=']='bool'
        Semantic_Cube.cube['int']['num']['==']='bool'
        Semantic_Cube.cube['int']['num']['!=']='bool'
        Semantic_Cube.cube['int']['num']['=']=None
        Semantic_Cube.cube['int']['num']['AND']=None
        Semantic_Cube.cube['int']['num']['OR']=None
        Semantic_Cube.cube['int']['text']['+']=None
        Semantic_Cube.cube['int']['text']['-']=None
        Semantic_Cube.cube['int']['text']['/']=None
        Semantic_Cube.cube['int']['text']['*']=None
        Semantic_Cube.cube['int']['text']['>']=None
        Semantic_Cube.cube['int']['text']['<']=None
        Semantic_Cube.cube['int']['text']['>=']=None
        Semantic_Cube.cube['int']['text']['<=']=None
        Semantic_Cube.cube['int']['text']['==']=None
        Semantic_Cube.cube['int']['text']['!=']=None
        Semantic_Cube.cube['int']['text']['=']=None
        Semantic_Cube.cube['int']['text']['AND']=None
        Semantic_Cube.cube['int']['text']['OR']=None
        Semantic_Cube.cube['int']['bool']['+']=None
        Semantic_Cube.cube['int']['bool']['-']=None
        Semantic_Cube.cube['int']['bool']['/']=None
        Semantic_Cube.cube['int']['bool']['*']=None
        Semantic_Cube.cube['int']['bool']['>']=None
        Semantic_Cube.cube['int']['bool']['<']=None
        Semantic_Cube.cube['int']['bool']['>=']=None
        Semantic_Cube.cube['int']['bool']['<=']=None
        Semantic_Cube.cube['int']['bool']['==']=None
        Semantic_Cube.cube['int']['bool']['!=']=None
        Semantic_Cube.cube['int']['bool']['=']=None
        Semantic_Cube.cube['int']['bool']['AND']=None
        Semantic_Cube.cube['int']['bool']['OR']=None
        Semantic_Cube.cube['num']['int']['+']='num'
        Semantic_Cube.cube['num']['int']['-']='num'
        Semantic_Cube.cube['num']['int']['/']='num'
        Semantic_Cube.cube['num']['int']['*']='num'
        Semantic_Cube.cube['num']['int']['>']='bool'
        Semantic_Cube.cube['num']['int']['<']='bool'
        Semantic_Cube.cube['num']['int']['>=']='bool'
        Semantic_Cube.cube['num']['int']['<=']='bool'
        Semantic_Cube.cube['num']['int']['==']='bool'
        Semantic_Cube.cube['num']['int']['!=']='bool'
        Semantic_Cube.cube['num']['int']['=']='num'
        Semantic_Cube.cube['num']['int']['AND']=None
        Semantic_Cube.cube['num']['int']['OR']=None
        Semantic_Cube.cube['num']['num']['+']='num'
        Semantic_Cube.cube['num']['num']['-']='num'
        Semantic_Cube.cube['num']['num']['/']='num'
        Semantic_Cube.cube['num']['num']['*']='num'
        Semantic_Cube.cube['num']['num']['>']='bool'
        Semantic_Cube.cube['num']['num']['<']='bool'
        Semantic_Cube.cube['num']['num']['>=']='bool'
        Semantic_Cube.cube['num']['num']['<=']='bool'
        Semantic_Cube.cube['num']['num']['==']='bool'
        Semantic_Cube.cube['num']['num']['!=']='bool'
        Semantic_Cube.cube['num']['num']['=']='num'
        Semantic_Cube.cube['num']['num']['AND']=None
        Semantic_Cube.cube['num']['num']['OR']=None
        Semantic_Cube.cube['num']['text']['+']=None
        Semantic_Cube.cube['num']['text']['-']=None
        Semantic_Cube.cube['num']['text']['/']=None
        Semantic_Cube.cube['num']['text']['*']=None
        Semantic_Cube.cube['num']['text']['>']=None
        Semantic_Cube.cube['num']['text']['<']=None
        Semantic_Cube.cube['num']['text']['>=']=None
        Semantic_Cube.cube['num']['text']['<=']=None
        Semantic_Cube.cube['num']['text']['==']=None
        Semantic_Cube.cube['num']['text']['!=']=None
        Semantic_Cube.cube['num']['text']['=']=None
        Semantic_Cube.cube['num']['text']['AND']=None
        Semantic_Cube.cube['num']['text']['OR']=None
        Semantic_Cube.cube['num']['bool']['+']=None
        Semantic_Cube.cube['num']['bool']['-']=None
        Semantic_Cube.cube['num']['bool']['/']=None
        Semantic_Cube.cube['num']['bool']['*']=None
        Semantic_Cube.cube['num']['bool']['>']=None
        Semantic_Cube.cube['num']['bool']['<']=None
        Semantic_Cube.cube['num']['bool']['>=']=None
        Semantic_Cube.cube['num']['bool']['<=']=None
        Semantic_Cube.cube['num']['bool']['==']=None
        Semantic_Cube.cube['num']['bool']['!=']=None
        Semantic_Cube.cube['num']['bool']['=']=None
        Semantic_Cube.cube['num']['bool']['AND']=None
        Semantic_Cube.cube['num']['bool']['OR']=None
        Semantic_Cube.cube['text']['int']['+']=None
        Semantic_Cube.cube['text']['int']['-']=None
        Semantic_Cube.cube['text']['int']['/']=None
        Semantic_Cube.cube['text']['int']['*']=None
        Semantic_Cube.cube['text']['int']['>']=None
        Semantic_Cube.cube['text']['int']['<']=None
        Semantic_Cube.cube['text']['int']['>=']=None
        Semantic_Cube.cube['text']['int']['<=']=None
        Semantic_Cube.cube['text']['int']['==']=None
        Semantic_Cube.cube['text']['int']['!=']=None
        Semantic_Cube.cube['text']['int']['=']=None
        Semantic_Cube.cube['text']['int']['AND']=None
        Semantic_Cube.cube['text']['int']['OR']=None
        Semantic_Cube.cube['text']['num']['+']=None
        Semantic_Cube.cube['text']['num']['-']=None
        Semantic_Cube.cube['text']['num']['/']=None
        Semantic_Cube.cube['text']['num']['*']=None
        Semantic_Cube.cube['text']['num']['>']=None
        Semantic_Cube.cube['text']['num']['<']=None
        Semantic_Cube.cube['text']['num']['>=']=None
        Semantic_Cube.cube['text']['num']['<=']=None
        Semantic_Cube.cube['text']['num']['==']=None
        Semantic_Cube.cube['text']['num']['!=']=None
        Semantic_Cube.cube['text']['num']['=']=None
        Semantic_Cube.cube['text']['num']['AND']=None
        Semantic_Cube.cube['text']['num']['OR']=None
        Semantic_Cube.cube['text']['text']['+']=None
        Semantic_Cube.cube['text']['text']['-']=None
        Semantic_Cube.cube['text']['text']['/']=None
        Semantic_Cube.cube['text']['text']['*']=None
        Semantic_Cube.cube['text']['text']['>']=None
        Semantic_Cube.cube['text']['text']['<']=None
        Semantic_Cube.cube['text']['text']['>=']=None
        Semantic_Cube.cube['text']['text']['<=']=None
        Semantic_Cube.cube['text']['text']['==']='bool'
        Semantic_Cube.cube['text']['text']['!=']='bool'
        Semantic_Cube.cube['text']['text']['=']='text'
        Semantic_Cube.cube['text']['text']['AND']=None
        Semantic_Cube.cube['text']['text']['OR']=None
        Semantic_Cube.cube['text']['bool']['+']=None
        Semantic_Cube.cube['text']['bool']['-']=None
        Semantic_Cube.cube['text']['bool']['/']=None
        Semantic_Cube.cube['text']['bool']['*']=None
        Semantic_Cube.cube['text']['bool']['>']=None
        Semantic_Cube.cube['text']['bool']['<']=None
        Semantic_Cube.cube['text']['bool']['>=']=None
        Semantic_Cube.cube['text']['bool']['<=']=None
        Semantic_Cube.cube['text']['bool']['==']=None
        Semantic_Cube.cube['text']['bool']['!=']=None
        Semantic_Cube.cube['text']['bool']['=']=None
        Semantic_Cube.cube['text']['bool']['AND']=None
        Semantic_Cube.cube['text']['bool']['OR']=None
        Semantic_Cube.cube['bool']['int']['+']=None
        Semantic_Cube.cube['bool']['int']['-']=None
        Semantic_Cube.cube['bool']['int']['/']=None
        Semantic_Cube.cube['bool']['int']['*']=None
        Semantic_Cube.cube['bool']['int']['>']=None
        Semantic_Cube.cube['bool']['int']['<']=None
        Semantic_Cube.cube['bool']['int']['>=']=None
        Semantic_Cube.cube['bool']['int']['<=']=None
        Semantic_Cube.cube['bool']['int']['==']=None
        Semantic_Cube.cube['bool']['int']['!=']=None
        Semantic_Cube.cube['bool']['int']['=']=None
        Semantic_Cube.cube['bool']['int']['AND']=None
        Semantic_Cube.cube['bool']['int']['OR']=None
        Semantic_Cube.cube['bool']['num']['+']=None
        Semantic_Cube.cube['bool']['num']['-']=None
        Semantic_Cube.cube['bool']['num']['/']=None
        Semantic_Cube.cube['bool']['num']['*']=None
        Semantic_Cube.cube['bool']['num']['>']=None
        Semantic_Cube.cube['bool']['num']['<']=None
        Semantic_Cube.cube['bool']['num']['>=']=None
        Semantic_Cube.cube['bool']['num']['<=']=None
        Semantic_Cube.cube['bool']['num']['==']=None
        Semantic_Cube.cube['bool']['num']['!=']=None
        Semantic_Cube.cube['bool']['num']['=']=None
        Semantic_Cube.cube['bool']['num']['AND']=None
        Semantic_Cube.cube['bool']['num']['OR']=None
        Semantic_Cube.cube['bool']['text']['+']=None
        Semantic_Cube.cube['bool']['text']['-']=None
        Semantic_Cube.cube['bool']['text']['/']=None
        Semantic_Cube.cube['bool']['text']['*']=None
        Semantic_Cube.cube['bool']['text']['>']=None
        Semantic_Cube.cube['bool']['text']['<']=None
        Semantic_Cube.cube['bool']['text']['>=']=None
        Semantic_Cube.cube['bool']['text']['<=']=None
        Semantic_Cube.cube['bool']['text']['==']=None
        Semantic_Cube.cube['bool']['text']['!=']=None
        Semantic_Cube.cube['bool']['text']['=']=None
        Semantic_Cube.cube['bool']['text']['AND']=None
        Semantic_Cube.cube['bool']['text']['OR']=None
        Semantic_Cube.cube['bool']['bool']['+']=None
        Semantic_Cube.cube['bool']['bool']['-']=None
        Semantic_Cube.cube['bool']['bool']['/']=None
        Semantic_Cube.cube['bool']['bool']['*']=None
        Semantic_Cube.cube['bool']['bool']['>']=None
        Semantic_Cube.cube['bool']['bool']['<']=None
        Semantic_Cube.cube['bool']['bool']['>=']=None
        Semantic_Cube.cube['bool']['bool']['<=']=None
        Semantic_Cube.cube['bool']['bool']['==']='bool'
        Semantic_Cube.cube['bool']['bool']['!=']='bool'
        Semantic_Cube.cube['bool']['bool']['=']='bool'
        Semantic_Cube.cube['bool']['bool']['AND']='bool'
        Semantic_Cube.cube['bool']['bool']['OR']='bool'

        