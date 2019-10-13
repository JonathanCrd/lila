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

    @staticmethod
    def add_function(function):
        '''
        Method to add a function into the function directory.
        It recieves an object Function to append, 
        if the function already exists, it will return false.
        '''
            
        if function.name not in Semantic.dirFunctions.keys():
            Semantic.dirFunctions[function.name] = function
            return True
        else:
            return False

    @staticmethod
    def add_var(var):
        '''
        Method to add a variable into the current scope table.
        It recieves an object Function to append, 
        if the function already exists, it will return false.
        '''
        if Semantic.isGlobal == True:
            #This is a global variable
            if var.name not in Semantic.varGlobals:
                Semantic.varGlobals[var.name] = var
                return True
            else:
                return False
        else:
            #This variable is inside an scope (It's a local variable)
            if var.name not in Semantic.varGlobals and var.name not in Semantic.varFunct:
                Semantic.varFunct[var.name] = var
                return True
            else:
                return False
    
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
    def look_for_variable(var):
        if var.name in Semantic.varGlobals.keys():
            return Semantic.varGlobals[var.name]
        else:
            if var.name in Semantic.varFunct.keys():
                return Semantic.varGlobals[var.name]
            else:
                return None

    @staticmethod
    def display_test():
        print("=============================")
        print("Dir de funciones: ")
        for x, y in Semantic.dirFunctions.items():
            print(x, y)
        print("\nVars Globales: ")
        for x, y in Semantic.varGlobals.items():
            print(x, y)
        print("\nVars Locales: ")
        for x, y in Semantic.varFunct.items():
            print(x, y)
        print("=============================")

