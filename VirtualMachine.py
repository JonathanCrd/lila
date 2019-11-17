class Memory:
    def __init__(self,mem_declaration):
        self.memory_declaration = dict((v, k) for k, v in mem_declaration.items())

        # Dictionaries used to store and handle in memory address
        self.memory = {
            'Global int'  : {},
            'Global num'  : {},
            'Global text' : {},
            'Global bool' : {},
            'Local int'   : {},
            'Local num'  : {},
            'Local text'  : {},
            'Local bool'  : {},
            'Temp int'  : {},
            'Temp num'  : {},
            'Temp text'  : {},
            'Temp bool'  : {},
            'Const int'  : {},
            'Const num'  : {},
            'Const text'  : {},
            'Const bool'  : {}
            }

        self.base_address = {
            'Global int'  : [0],
            'Global num'  : [0],
            'Global text' : [0],
            'Global bool' : [0],
            'Local int'   : [0],
            'Local num'  : [0],
            'Local text'  : [0],
            'Local bool'  : [0],
            'Temp int'  : [0],
            'Temp num'  : [0],
            'Temp text'  : [0],
            'Temp bool'  : [0],
            'Const int'  : [0],
            'Const num'  : [0],
            'Const text'  : [0],
            'Const bool'  : [0]
        }
  
    def address_translation(self,address):
        '''
        Method to translate relative addresses from the quadruples to actual location within the memory
        '''
        print(address)
        address_type = int(address / 1000)
        address_type = address_type * 1000
        address_type = self.memory_declaration[address_type]
        
        actual_location = address % 1000
        
        return (address_type, actual_location)
    
    def memory_bounds(self, address, address_type):
        '''
        Auxiliar method that verifies that the address wich is going to be used for writing is not out of bounds
        '''
        actual_location = address % 1000
        actual_location = actual_location + self.base_address[address_type][-1]
        address = int(address / 1000)
        final_address = int(((address * 1000) + actual_location )/1000) * 1000

        if final_address in self.memory_declaration:
            final_address = self.memory_declaration[final_address]
        else:
            while(final_address not in self.memory_declaration):
                final_address -= 1000
            final_address = self.memory_declaration[final_address]
        
        if final_address != address_type:
            raise MemoryError("Out of bounds.")
        
    def read(self, address):
        '''
        Method that returns the value inside an specific memory address given as an input.
        '''
        # print(self.memory)
        address_type, actual_location = self.address_translation(address)
        if actual_location in self.memory[address_type]:
            return self.memory[address_type][actual_location]
        else:
            print(address,address_type,actual_location)
            raise MemoryError("Value not declared.")
                
        
    def write(self, address, input):
        '''
        Method that writes a given input inside an specified memory address
        It verifies that there is not out of bounds memory error
        '''
        address_type, actual_location = self.address_translation(address)
        self.memory_bounds(address,address_type)

        self.memory[address_type][actual_location] = input

    def era_statement(self, memory_required):
        '''
        Method to prepare memory in a call. It receaives the memory needed for each type and add those to the pointer stack.
        '''
        self.base_address['Local int'].append(memory_required['int'] + self.base_address['Local int'][-1])
        self.base_address['Local num'].append(memory_required['num'] + self.base_address['Local num'][-1])
        self.base_address['Local text'].append(memory_required['text'] + self.base_address['Local text'][-1])
        self.base_address['Local bool'].append(memory_required['bool'] + self.base_address['Local bool'][-1])
        self.base_address['Temp int'].append(memory_required['Temp int'] + self.base_address['Temp int'][-1])
        self.base_address['Temp num'].append(memory_required['Temp num'] + self.base_address['Temp num'][-1])
        self.base_address['Temp text'].append(memory_required['Temp text'] + self.base_address['Temp text'][-1])
        self.base_address['Temp bool'].append(memory_required['Temp bool'] + self.base_address['Temp bool'][-1])

        print(self.base_address)

    def clean_base_addresses(self):
        '''
        Method to pop the last base addreses of each type.
        Call this method at the end of a function.
        '''
        for key in self.base_address.items():
            self.base_address[key].pop()
        
        

class VirtualMachine:
    def __init__(self, obj : list ):
        '''
        Virtual machine to execute the Lila programming language code.
        It takes as a parameter an obj containing the quadruples, function directory, global variables and constant table. 
        '''
        self.total_quadruples = obj[0]
        self.quadruples = obj[1]
        self.constants_table = obj[2]
        self.dir_functions = obj[3]
        self.global_vars = obj[4]
        self.memory_declaration = obj[5]
        self.memory = Memory(self.memory_declaration)
        self.pointer_stack = [0] # This will point to the quadruple to execute

        self.write_const()

    def write_const(self):
        print(self.constants_table)
        for key,value in self.constants_table.items():
            if str(value[0]) == 'int':
                self.memory.write(value[1],int(key))
            if str(value[0]) == 'text':
                self.memory.write(value[1],str(key))
            if str(value[0]) == 'num':
                self.memory.write(value[1],float(key))
            if str(value[0]) == 'bool':
                if str(key) == 'TRUE':
                    self.memory.write(value[1],True)
                else:
                    self.memory.write(value[1],False)

    def quadruples_handler(self):
        '''
        Calls the proper method according to the operand/code in the first position of each quadruple.
        '''
        while(self.pointer_stack[-1] < self.total_quadruples):
            print(self.pointer_stack[-1], self.quadruples[self.pointer_stack[-1]].operator)
            quadruple = self.quadruples[self.pointer_stack[-1]]
            
            if (quadruple.operator == '+' or quadruple.operator == '-'  or quadruple.operator == '*' or quadruple.operator == '/'):
                self.arithmetic()
            elif (quadruple.operator == '='):
                self.assign()
            elif (quadruple.operator == 'DISPLAY'):
                pass
            elif (quadruple.operator == 'INPUT'):
                pass
            elif (quadruple.operator == 'RETURN'):
                pass
            elif (quadruple.operator == 'GOTOF'):
                self.go_to_f()
                self.pointer_stack[-1] -= 1
                pass
            elif (quadruple.operator == 'GOTO'):
                self.go_to()
                self.pointer_stack[-1] -= 1
            elif (quadruple.operator == 'GOTOSUB'):
                self.pointer_stack[-1] -= 1
                pass
            elif (quadruple.operator == 'ERA'):
                pass
            elif (quadruple.operator == 'PARAM'):
                pass
            elif (quadruple.operator == 'ENDPROC'):
                pass
            elif (quadruple.operator == 'END'):
                pass
            else:
                pass
            
            self.pointer_stack[-1] += 1
        
        print("HOLA")
        # print(self.memory.memory)


    # MATH
    def assign(self):
        left = self.memory.read(self.quadruples[self.pointer_stack[-1]].left.memory)
        resultAddress = self.quadruples[self.pointer_stack[-1]].resultado.memory
        resultType = self.quadruples[self.pointer_stack[-1]].resultado.v_type
        casting = {"int": (lambda x: int(x)),"num": (lambda x: float(x)),"text": (lambda x: str(x)),"bool": (lambda x: make_bool(x)),}
        result = casting[resultType](left)
        print("MemoriaAssign", left, resultAddress)
        self.memory.write(resultAddress,result)

    def arithmetic(self):
        op = self.quadruples[self.pointer_stack[-1]].operator
        left = self.memory.read(self.quadruples[self.pointer_stack[-1]].left.memory)
        right = self.memory.read(self.quadruples[self.pointer_stack[-1]].right.memory)
        resultAddress = self.quadruples[self.pointer_stack[-1]].resultado.memory
        resultType = self.quadruples[self.pointer_stack[-1]].resultado.v_type
        print("MemoriaArithmetic", left, resultAddress)
        operations = { 
                "+": (lambda x,y: x+y), 
                "-": (lambda x,y: x-y),
                "*": (lambda x,y: x*y),
                "/": (lambda x,y: self.op_div(x,y)) 
              } 
        casting = {"int": (lambda x: int(x)),"num": (lambda x: float(x)),"text": (lambda x: str(x)),"bool": (lambda x: make_bool(x)),}
        result = operations[op](left,right)
        result = casting[resultType](result)
        self.memory.write(resultAddress,result)

    def op_div(self,x,y):
        if x == 0:
            raise ZeroDivisionError("Division by 0 isn't possible")
        else:
            return x/y

    def make_bool(self,x):
        if x=="TRUE":
            return True
        elif x=="FALSE":
            return False
        else:
            raise TypeError("Booleano incorrecto")

    def go_to(self):
        self.pointer_stack[-1] = self.quadruples[self.pointer_stack[-1]].resultado.value - 1

    def go_to_f(self):
        value = self.quadruples[self.pointer_stack[-1]].left.value
        b_value = self.make_bool(value)
        if(not b_value):
            self.pointer_stack[-1] = self.quadruples[self.pointer_stack[-1]].resultado.value - 1
            

