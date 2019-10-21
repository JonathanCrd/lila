class Function:
    def __init__(self, name, f_type):
        self.name = name
        self.f_type = f_type
        self.num_params = 0

class Var:
    def __init__(self, name, v_type, value):
        self.name = name
        self.v_type = v_type
        self.value = value

class Semantic:
    dirFunctions = dict()
    varGlobals = dict()
    varFunct = dict()
    isGlobal = True
    lastFuncKey = None

    @staticmethod
    def enterFunciones(name,tipo,void):
        if(void == None):
           funcTemp = Function(name,tipo)
        else:
           funcTemp = Function(name,void)
     
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
                Semantic.varGlobals[var.name] = var
            else:
                raise SyntaxError("Variable " + var.name  + " is already declared in the global scope")
        else:
            #This variable is inside an scope (It's a local variable)
            if var.name not in Semantic.varGlobals and var.name not in Semantic.varFunct:
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
            Semantic.varFunct[var.name] = var
            Semantic.dirFunctions[Semantic.lastFuncKey].num_params += 1
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
    def look_for_function(function):
        #validate that the function exists
        if function.name in Semantic.dirFunctions.keys():
            return Semantic.dirFunctions[function.name]
        else:
            return None

    @staticmethod
    def look_for_variable(var_name:str):
        if var_name in Semantic.varGlobals.keys():
            return Semantic.varGlobals[var_name]
        else:
            if var_name in Semantic.varFunct.keys():
                return Semantic.varFunct[var_name]
            else:
                raise SyntaxError("Variable '" + var_name  + "' not declared.")

    @staticmethod
    def display_test():
        print("=============================")
        print("Dir de funciones: ")
        for x, y in Semantic.dirFunctions.items():
            print(x, y.name, y.f_type, y.num_params)
        print("\nVars Globales: ")
        for x, y in Semantic.varGlobals.items():
            print(x, y.name, y.v_type, y.value)
        print("\nVars Locales: ")
        for x, y in Semantic.varFunct.items():
            print(x, y.name, y.v_type, y.value)
        print("=============================")

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

        