class Function:
    def __init__(self, name, f_type, index):
        self.name = name
        self.f_type = f_type
        self.quadruple_index = index
        self.params = []
        self.memory_required = {}

class Operand:
    def __init__(self, name, v_type, value):
        self.name = name
        self.v_type = v_type
        self.value = value
        self.memory = None
        self.array = None
        self.pointer = False

class DimensionStruct:
    def __init__(self,upper_limit):
        self.upper_limit = upper_limit
        self.m = None

class VirtualAddress:
    memory_declaration = {
        'Global int'    : 4000, #4000
        'Global num'    : 6000,
        'Global text'   : 8000,
        'Global bool'   : 10000,
        'Local int'     : 20000, #20000
        'Local num'     : 22000,
        'Local text'    : 24000,
        'Local bool'    : 26000,
        'Temp int'      : 30000, #30000
        'Temp num'      : 32000,
        'Temp text'     : 34000,
        'Temp bool'     : 36000, #36000
        'Const int'     : 40000, #40000
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

    aux = 1
    @staticmethod
    def getAddress(a_type):
        '''
        Return the next available address for an specific type.
        '''
        tempAdress = VirtualAddress.memory_declaration[a_type] + VirtualAddress.counters[a_type]
        VirtualAddress.counters[a_type] += VirtualAddress.aux
        return tempAdress

    @staticmethod
    def getConstantAddress(a_type):
        tempAdress = VirtualAddress.memory_declaration[a_type] + VirtualAddress.counters[a_type]
        VirtualAddress.counters[a_type] += 1

        return tempAdress
    
    @staticmethod
    def resetLocals():
        VirtualAddress.counters['Local int'] = 0
        VirtualAddress.counters['Local num'] = 0
        VirtualAddress.counters['Local text'] = 0
        VirtualAddress.counters['Local bool'] = 0
        VirtualAddress.counters['Temp int'] = 0
        VirtualAddress.counters['Temp num'] = 0
        VirtualAddress.counters['Temp text'] = 0
        VirtualAddress.counters['Temp bool'] = 0

class ERA:
    '''
    Class for keeping track of the memory needed for an specific function
    '''
    def __init__(self):
        self.var_counters = {
        'int'     : 0,
        'num'     : 0,
        'text'    : 0,
        'bool'    : 0,
        'Temp int'      : 0,
        'Temp num'      : 0,
        'Temp text'     : 0,
        'Temp bool'     : 0
    }

class Semantic:
    dirFunctions = dict()
    varGlobals = dict()
    varFunct = dict()
    isGlobal = True
    lastFuncKey = None
    Era = None

    #Handle arrays
    dims = None
    dim_counter = 0
    total_dims = []
    arr_r = 0

    @staticmethod
    def enterFunciones(name,tipo,void,index):
        '''
        Method to check if the function is already defined. If not, a new ERA instance is created.
        '''
        if(void == None):
           funcTemp = Function(name,tipo,index)
        else:
           funcTemp = Function(name,void,index)
     
        if (Semantic.add_function(funcTemp) == False):
             # This means that the function is already defined in the program
            raise SyntaxError("Function " + name + " is already defined")
        
        # Create new ERA instance for the counters of this function
        Semantic.Era = ERA()
            
    @staticmethod
    def add_function(function:Function):
        '''
        Method to add a function into the function directory.
        It recieves an object Function to append, 
        if the function already exists, it will return false.
        '''
            
        if function.name not in Semantic.dirFunctions.keys():
            Semantic.dirFunctions[function.name] = function
            Semantic.lastFuncKey = function.name
            if function.f_type != 'void':
                Semantic.isGlobal=True
                Semantic.add_var(Operand(function.name,function.f_type,None))
                Semantic.isGlobal=False
            return True
        else:
            return False

    @staticmethod
    def add_var(var:Operand):
        '''
        Method to add a variable into the current scope table.
        It recieves an object Variable to append.
        '''

        var.array = Semantic.dims

        if Semantic.isGlobal == True:
            #This is a global variable
            if var.name not in Semantic.varGlobals:
                #Asociate it with a global dir
                var.memory = VirtualAddress.getAddress('Global '+ str(var.v_type))
                Semantic.varGlobals[var.name] = var
            else:
                raise SyntaxError("Variable " + var.name  + " is already declared in the global scope")
        else:
            #This variable is inside an scope (It's a local variable)
            if var.name not in Semantic.varGlobals and var.name not in Semantic.varFunct:
                 #Asociar direccion virtual local
                var.memory = VirtualAddress.getAddress('Local '+ str(var.v_type))
                Semantic.varFunct[var.name] = var
                Semantic.Era.var_counters[var.v_type] += 1
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
            Semantic.Era.var_counters[var.v_type] += 1
            Semantic.dirFunctions[Semantic.lastFuncKey].params.append(var)
        else:
            raise SyntaxError("Variable " + var.name  + " is already declared in the actual scope")
    
    @staticmethod
    def end_function():
        '''
        Method to assign the counters of the variables needed in this function to that function and
        dump the variables table when function is no longer needed.
        '''
        Semantic.dirFunctions[Semantic.lastFuncKey].memory_required = Semantic.Era.var_counters
        Semantic.varFunct = {}
    
    @staticmethod
    def look_for_function(function_name:str):
        '''
        Validates that a function exists (function name is given as parameter) exists in the directory of Functions.
        If it exists, it returns the function object, if not it raises an error.
        '''
        if function_name in Semantic.dirFunctions.keys():
            return Semantic.dirFunctions[function_name]
        else:
            raise SyntaxError("Function '" + function_name  + "' is not declared.")

    @staticmethod
    def look_for_variable(var_name:str):
        '''
        Checks if a variables (given as parameter) exists either in Table of Globals or Table of locals
        If it exists, it returns the variable, if not it raises an error.
        '''
        if var_name in Semantic.varGlobals.keys():
            return Semantic.varGlobals[var_name]
        else:
            if var_name in Semantic.varFunct.keys():
                return Semantic.varFunct[var_name]
            else:
                raise SyntaxError("Variable '" + var_name  + "' is not declared.")

    @staticmethod
    def checkReturn(last_type):
        '''
        Check if the Return statement can be performed in the current context.
        '''
        if(Semantic.lastFuncKey == None):
            raise SyntaxError("Block main can't have a return")

        func_type = Semantic.dirFunctions[Semantic.lastFuncKey].f_type
        if func_type == 'void':
            raise SyntaxError("Function of type '"+ func_type + "' can't have a return")
        if func_type != last_type.v_type:
            raise SyntaxError("Function of type '"+ func_type + "' must return same type, can't return '" + last_type.v_type +"'")

    @staticmethod
    def isVoid(funct_name:str,expected:bool):
        '''
        Check if the  function is void and depending on it expected value will raise an exception.
        Expected True means that the function is espected to be void.
        != void y quiera void -> invocacion OR  != void y no quiera void -> asignacion OR 
        '''
        f_type = Semantic.dirFunctions[funct_name].f_type
        if f_type != 'void' and expected:
            raise SyntaxError("Function '" + funct_name + "' must be assigned to a variable since it is not void")
        else:
            if f_type == 'void' and not(expected):
                raise SyntaxError("Function '" + funct_name + "' cannot be used as operand since it is void")
    
    @staticmethod
    def array_declaration():
        '''
        Initialize the vars needed at the begining of array declarations.
        '''
        Semantic.dims = []
        Semantic.dim_counter = 1
        Semantic.arr_r = 1
    
    @staticmethod
    def array_dimension(upper_limit):
        '''
        Creates the structure with the upper limit and recalculates R.
        '''
        upper_limit = int(upper_limit) - 1 # Adjust the upper_limit with a base of 0, like Cpp

        # Check if the limit is at least 1
        if (upper_limit < 0):
            raise IndexError("Error, arrays should be at least size of 1.")

        dim_temp = DimensionStruct(upper_limit)
        Semantic.dims.append(dim_temp)
        Semantic.arr_r = (upper_limit + 1) * Semantic.arr_r

    @staticmethod
    def array_next_dim():
        '''
        Add 1 to the dim size of the current array.
        '''
        Semantic.dim_counter += 1

    @staticmethod
    def addConstWithoutStack(constant):
        ##Search if the constant already exists
        constant = str(int(constant))
        if constant not in VirtualAddress.constants_table:
            VirtualAddress.constants_table[constant] = ['int', VirtualAddress.getConstantAddress('Const ' + str('int'))]

    
    @staticmethod
    def arr_second_round():
        '''
        Calculate the m for each dimension.
        In this case, K it is not important since the lower limit is always 0.
        '''
        VirtualAddress.aux = Semantic.arr_r
        k = 0
        Semantic.dim_counter = 1
        for item in Semantic.dims:
            item.m = Semantic.arr_r / (item.upper_limit + 1)
            Semantic.addConstWithoutStack(item.m)
            Semantic.arr_r = item.m
    
    @staticmethod
    def reset_array_setup():
        '''
        At the end of the statement, resets the vars needed for array handling.
        '''
        Semantic.dims = None
        Semantic.dim_counter = 0
        Semantic.arr_r = 0
        Semantic.total_dims = []
        VirtualAddress.aux = 1

    @staticmethod
    def check_var_dim(var_id):
        '''
        Check if the variable given is a dimensioned one. If not, raise an exception.
        '''
        var_temp = Semantic.look_for_variable(var_id)
        if (var_temp.array is None):
            raise AttributeError("Error, variable '" + str(var_id) + "' is not a dimensioned.")
        
    @staticmethod
    def check_dims(var_id):
        '''
        Check if the dimension given exists in the variable given. If not, raise an exception.
        '''
        var_temp = Semantic.look_for_variable(var_id)
        if(Semantic.total_dims[-1] != len(var_temp.array)):
            raise KeyError("Error in dimensions of '" + str(var_id) + "'")

        Semantic.total_dims.pop()

    @staticmethod
    def checkMoreDims(var_id):
        '''
        Check if the dimension given exists in the variable given. If not, raise an exception.
        '''
        var_temp = Semantic.look_for_variable(var_id)
        if(Semantic.total_dims[-1] > len(var_temp.array)):
            raise KeyError("Error in dimensions of '" + str(var_id) + "'")

    @staticmethod
    def count_dim(var_id):
        Semantic.total_dims[-1] += 1

    @staticmethod   
    def checkSpecialParam(var_name):
        '''
        Checks that ID given as parameter for special function is of only one dimension
        Also checks that it's of type int or num
        '''
        var_temp = Semantic.look_for_variable(var_name)
        Semantic.check_var_dim(var_temp.name)

        if 1 != len(var_temp.array):
            raise TypeError("This function expects an array of only 1 dimension")

        if var_temp.v_type != 'int' and var_temp.v_type != 'num':
            raise TypeError("This function expects an array of type int or num")

    
    @staticmethod  
    def checkIsOneDim(var_name):
        '''
        Checks that ID given as parameter for special function is of only one dimension
        '''
        var_temp = Semantic.look_for_variable(var_name)
        Semantic.check_var_dim(var_temp.name)

        if 1 != len(var_temp.array):
            raise TypeError("This function expects an array of only 1 dimension")
    
    @staticmethod
    def display_test():
        # print("=============================")
        # print("DIR FUNCIONES: ")
        # for x, y in Semantic.dirFunctions.items():
        #     print(x, y.name, y.f_type, len(y.params), y.memory_required)
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

        