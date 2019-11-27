import numpy as np
import statistics as stat
import pandas as pd
import matplotlib.pyplot as plt

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

        self.next_base_address = {
            'Local int'   : [0],
            'Local num'  : [0],
            'Local text'  : [0],
            'Local bool'  : [0],
            'Temp int'  : [0],
            'Temp num'  : [0],
            'Temp text'  : [0],
            'Temp bool'  : [0]
        }
  
    def address_translation(self,address):
        '''
        Method to translate relative addresses from the quadruples to actual location within the memory
        '''
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
        address_type, actual_location = self.address_translation(address)
        actual_location = actual_location + self.base_address[address_type][-1]
        if actual_location in self.memory[address_type]:
            return self.memory[address_type][actual_location]
        else:
            raise MemoryError("Value not declared.")
                     
    def write(self, address, input):
        '''
        Method that writes a given input inside an specified memory address
        It verifies that there is not out of bounds memory error
        '''
        address_type, actual_location = self.address_translation(address)
        self.memory_bounds(address,address_type)
        actual_location = actual_location + self.base_address[address_type][-1]
        self.memory[address_type][actual_location] = input

    def era_statement(self, memory_required):
        '''
        Method to prepare memory in a call. It receaives the memory needed for each type and add those to the pointer stack.
        '''
        self.base_address['Local int'].append(self.next_base_address['Local int'][-1])
        self.base_address['Local num'].append(self.next_base_address['Local num'][-1])
        self.base_address['Local text'].append(self.next_base_address['Local text'][-1])
        self.base_address['Local bool'].append(self.next_base_address['Local bool'][-1])
        self.base_address['Temp int'].append(self.next_base_address['Temp int'][-1])
        self.base_address['Temp num'].append(self.next_base_address['Temp num'][-1])
        self.base_address['Temp text'].append(self.next_base_address['Temp text'][-1])
        self.base_address['Temp bool'].append(self.next_base_address['Temp bool'][-1])

        self.next_base_address['Local int'].append(memory_required['int'] + self.next_base_address['Local int'][-1])
        self.next_base_address['Local num'].append(memory_required['num'] + self.next_base_address['Local num'][-1])
        self.next_base_address['Local text'].append(memory_required['text'] + self.next_base_address['Local text'][-1])
        self.next_base_address['Local bool'].append(memory_required['bool'] + self.next_base_address['Local bool'][-1])
        self.next_base_address['Temp int'].append(memory_required['Temp int'] + self.next_base_address['Temp int'][-1])
        self.next_base_address['Temp num'].append(memory_required['Temp num'] + self.next_base_address['Temp num'][-1])
        self.next_base_address['Temp text'].append(memory_required['Temp text'] + self.next_base_address['Temp text'][-1])
        self.next_base_address['Temp bool'].append(memory_required['Temp bool'] + self.next_base_address['Temp bool'][-1])
        
    def dump_memory_stack(self):
        '''
        Method to pop the last base addreses and next base address of each type.
        Call this method at the end of a function.
        '''
        
        for key,_ in self.next_base_address.items():
            self.next_base_address[key].pop()
            self.base_address[key].pop()
        
class VirtualMachine:
    def __init__(self, obj : list ):
        '''
        Virtual machine to execute the Lila programming language code.
        It takes as a parameter an obj containing the quadruples, function directory, global variables and constant table. 
        '''
        self.quadruples = obj['quadruples']
        self.constants_table = obj['constant_table']
        self.dir_functions = obj['dir_functions']
        memory_declaration = obj['memory_declaration']
        self.memory = Memory(memory_declaration)
        main_memory_required = obj['dir_functions']['main'].memory_required # Setting the point in which the next call to a function wil be based on memory
        
        self.pointer_stack = [0] # This will point to the quadruple to execute
        self.call_stack = [] # This saves all the function calls
        self.params_stack = []
        self.write_const()
        self.memory.era_statement(main_memory_required)
        self.prepare_memory = {}

    def write_const(self):
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
        while(self.pointer_stack[-1] < len(self.quadruples)):
            quadruple = self.quadruples[self.pointer_stack[-1]]
            
            if (quadruple.operator == '+' or quadruple.operator == '-'  or quadruple.operator == '*' or quadruple.operator == '/' or quadruple.operator == '<' or quadruple.operator == '>'  or quadruple.operator == '<=' or quadruple.operator == '>=' or quadruple.operator == '!=' or quadruple.operator == '==' or quadruple.operator == 'AND' or quadruple.operator == 'OR'):
                self.arithmetic()
            elif (quadruple.operator == '='):
                self.assign()
            elif (quadruple.operator == 'DISPLAY'):
                self.display()
            elif (quadruple.operator == 'INPUT'):
                self.op_input()
            elif (quadruple.operator == 'RETURN'):
                self.op_return()
            elif (quadruple.operator == 'GOTOF'):
                self.go_to_f()
            elif (quadruple.operator == 'GOTO'):
                self.go_to()
                self.pointer_stack[-1] -= 1
            elif (quadruple.operator == 'GOSUB'):
                self.go_sub()
                self.pointer_stack[-1] -= 1
            elif (quadruple.operator == 'ERA'):
                self.era()
            elif (quadruple.operator == 'PARAM'):
                self.params()
            elif (quadruple.operator == 'ENDPROC'):
                self.end_procedure()
            elif (quadruple.operator == 'NEGATIVE'):
                self.makeNegative()
            elif (quadruple.operator == '+BASE'):
                self.sum_base()
            elif (quadruple.operator == 'VER'):
                self.verify()
            elif (quadruple.operator == 'MEAN'):
                self.q_mean()
            elif (quadruple.operator == 'MEDIAN'):
                self.q_median()
            elif (quadruple.operator == 'MODE'):
                self.q_mode()
            elif (quadruple.operator == 'MIN'):
                self.q_min()
            elif (quadruple.operator == 'MAX'):
                self.q_max()
            elif (quadruple.operator == 'RANGE'):
                self.q_range()
            elif (quadruple.operator == 'DESESTANDAR'):
                self.q_desestandar()
            elif (quadruple.operator == 'PRINTMEASURES'):
                self.q_measures()
            elif (quadruple.operator == 'GETOUTLIERS'):
                self.q_getOutliers()
            elif (quadruple.operator == 'REMOVEOUTLIERS'):
                self.q_removeOutliers()
            elif (quadruple.operator == 'END'):
                print('SE ACABO')
                pass
            else:
                pass
            
            self.pointer_stack[-1] += 1
        
    def sum_base(self):
        left = self.memory.read(self.quadruples[self.pointer_stack[-1]].left.memory)
        right = self.quadruples[self.pointer_stack[-1]].right.memory
        
        resultAddress = self.quadruples[self.pointer_stack[-1]].resultado.memory
        resultType = self.quadruples[self.pointer_stack[-1]].resultado.v_type
        result = left + right
        self.memory.write(resultAddress,result)

    def verify(self):
        if (self.quadruples[self.pointer_stack[-1]].left.pointer):
            size = self.memory.read(self.memory.read(self.quadruples[self.pointer_stack[-1]].left.memory))
        else:
            size = self.memory.read(self.quadruples[self.pointer_stack[-1]].left.memory)
        lowerLimit = self.quadruples[self.pointer_stack[-1]].right
        upperLimit = self.quadruples[self.pointer_stack[-1]].resultado
        if (size < lowerLimit or size > upperLimit):
            raise IndexError("Index out of bounds.")

    def makeNegative(self):
        left = self.memory.read(self.quadruples[self.pointer_stack[-1]].left.memory)
        resultAddress = self.quadruples[self.pointer_stack[-1]].resultado.memory
        resultType = self.quadruples[self.pointer_stack[-1]].resultado.v_type
        casting = {"int": (lambda x: int(x)),"num": (lambda x: float(x))}
        result = left*-1
        self.memory.write(resultAddress,result)
        
    def assign(self):
        left = self.memory.read(self.quadruples[self.pointer_stack[-1]].left.memory)
        resultAddress = self.quadruples[self.pointer_stack[-1]].resultado.memory
        resultType = self.quadruples[self.pointer_stack[-1]].resultado.v_type

        if (self.quadruples[self.pointer_stack[-1]].left.pointer):
            left = self.memory.read(left)
        if (self.quadruples[self.pointer_stack[-1]].resultado.pointer):
            resultAddress =  self.memory.read(resultAddress)

        casting = {"int": (lambda x: int(x)),"num": (lambda x: float(x)),"text": (lambda x: str(x)),"bool": (lambda x: make_bool(x))}
        result = casting[resultType](left)
        self.memory.write(resultAddress,result)

    def arithmetic(self):

        op = self.quadruples[self.pointer_stack[-1]].operator
        left = self.memory.read(self.quadruples[self.pointer_stack[-1]].left.memory)
        right = self.memory.read(self.quadruples[self.pointer_stack[-1]].right.memory)
        resultAddress = self.quadruples[self.pointer_stack[-1]].resultado.memory
        resultType = self.quadruples[self.pointer_stack[-1]].resultado.v_type
        
        if (self.quadruples[self.pointer_stack[-1]].left.pointer):
            left = self.memory.read(left)
        if (self.quadruples[self.pointer_stack[-1]].right.pointer):
            right = self.memory.read(right)
        if (self.quadruples[self.pointer_stack[-1]].resultado.pointer):
            resultAddress =  self.memory.read(resultAddress)
        
        operations = { 
                "+": (lambda x,y: x+y), 
                "-": (lambda x,y: x-y),
                "*": (lambda x,y: x*y),
                "/": (lambda x,y: self.op_div(x,y)) ,
                "<": (lambda x,y: True if x<y else False),
                ">": (lambda x,y: True if x>y else False),
                "!=": (lambda x,y: True if x!=y else False),
                "==": (lambda x,y: True if x==y else False),
                "<=": (lambda x,y: True if x<=y else False),
                ">=": (lambda x,y: True if x>=y else False),
                "AND": (lambda x,y: True if x and y else False),
                "OR": (lambda x,y: True if x or y else False)
              } 

        casting = {"int": (lambda x: int(x)),"num": (lambda x: float(x)),"text": (lambda x: str(x)),"bool": (lambda x: self.make_bool(x))}
        result = operations[op](left,right)
        result = casting[resultType](result)
        self.memory.write(resultAddress,result)

    def op_div(self,x,y):
        if x == 0:
            raise ZeroDivisionError("Division by 0 isn't possible")
        else:
            return x/y

    def make_bool(self,x):
        if x=="TRUE" or x is True:
            return True
        elif x=="FALSE" or x is False:
            return False
        else:
            raise TypeError("Booleano incorrecto")

    def go_to(self):
        self.pointer_stack[-1] = self.quadruples[self.pointer_stack[-1]].resultado.value - 1

    def go_to_f(self):
        value = self.memory.read(self.quadruples[self.pointer_stack[-1]].left.memory)
        if(not value):
            self.pointer_stack[-1] = self.quadruples[self.pointer_stack[-1]].resultado.value - 1
            self.pointer_stack[-1] -= 1

    def display(self):
        index = self.pointer_stack[-1]
        resultAddress = self.memory.read(self.quadruples[index].resultado.memory)
        if (self.quadruples[index].resultado.pointer):
            resultAddress =  self.memory.read(resultAddress)
        print(resultAddress)

    def op_input(self):
        index = self.pointer_stack[-1]
        address = self.quadruples[index].resultado.memory
        message = self.quadruples[index].resultado.value
        i_type = self.quadruples[index].resultado.v_type
        if message == None:
            value = input()
        else:
            value = input(message)
        try:
            if i_type == 'int':
                value = int(value)
            elif i_type == 'num':
                value = float(value)
            elif i_type == 'text':
                value = str(value)
            elif i_type == 'bool':
                value = self.make_bool(value)
            else:
                raise Exception("Input not identified.")
        except Exception as err:
            raise err
        
        self.memory.write(address,value)
    
    def era(self):
        '''
        Requests space for execution when a function is called.
        '''
        funcName = self.quadruples[self.pointer_stack[-1]].resultado
        self.prepare_memory = self.dir_functions[funcName].memory_required
    
    def go_sub(self):
        '''
        Adds the name of the function called to the call stack and changes the current quadruple index.
        '''
        self.memory.era_statement(self.prepare_memory)

        aux_pointer = self.pointer_stack[-1]
        # self.pointer_stack[-1] += 1
        funcName = self.quadruples[aux_pointer].resultado.name
        self.call_stack.append(funcName) # Append the function name to the call stack
        self.setParams(funcName)
        self.pointer_stack.append(self.quadruples[aux_pointer].resultado.value - 1)

    def setParams(self, funcName):
        reversedParams = self.dir_functions[funcName].params
        reversedParams.reverse()
        for param in self.dir_functions[funcName].params:
            self.memory.write(param.memory, self.params_stack.pop())

    def op_return(self):
        '''
        Assign the value of the return to the global variable with the name of the current function.
        The current function must not be a void one since the return statement is not valid in void functions.
        '''
        index = self.pointer_stack[-1]
        address = self.quadruples[index].left.memory
        value = self.memory.read(address)

        assign_address = self.quadruples[index].resultado
        self.memory.write(assign_address,value)

        self.end_procedure()
        
    def end_procedure(self):
        self.pointer_stack.pop()
        self.memory.dump_memory_stack()
        self.call_stack.pop()
    
    def params(self):
        '''
        Each time a parameter is send, it will get the value and assign it to the list of parameters
        '''
        index = self.pointer_stack[-1]
        paramValue = self.memory.read(self.quadruples[index].left.memory)
        self.params_stack.append(paramValue)

    def read_array(self):
        '''
        Read the array specified in the next quadruple.
        '''
        array_temp = []
        self.pointer_stack[-1] += 1
        quadruple = self.quadruples[self.pointer_stack[-1]]
        base_address = quadruple.left
        size = quadruple.left + quadruple.right

        for x in range(base_address,size+1):
            temp = self.memory.read(x)
            if(temp is not None):
                array_temp.append(temp)

        return array_temp

    def q_mean(self):
        '''
        Print the mean of an array. 
        '''
        array_temp = self.read_array()
        print(np.mean(array_temp))
        
    def q_median(self):
        '''
        Print the median of an array. 
        '''
        array_temp = self.read_array()
        print(np.median(array_temp))

    def q_mode(self):
        '''
        Print the mode of an array. 
        '''
        array_temp = self.read_array()
        try:
            print(stat.mode(array_temp))
        except:
            print("There is no mode.")
    
    def q_min(self):
        '''
        Print the min value of an array. 
        '''
        array_temp = self.read_array()
        print(min(array_temp))
    
    def q_max(self):
        '''
        Print the max value of an array. 
        '''
        array_temp = self.read_array()
        print(max(array_temp))
    
    def q_range(self):
        '''
        Print the range of an array. 
        '''
        array_temp = self.read_array()
        rango = max(array_temp) - min(array_temp)
        print(rango)

    def q_desestandar(self):
        '''
        Print the standard deviation of an array. 
        '''
        array_temp = self.read_array()
        print(stat.stdev(array_temp))
    
    def q_measures(self):
        '''
        Print the measures of an array. 
        '''
        array_temp = self.read_array()
        print("Measures of data: /n")
        print("Mean: ", np.mean(array_temp))
        print("Median: ", np.median(array_temp))
        print("Mode: ", stat.mode(array_temp))
        rango = max(array_temp) - min(array_temp)
        print("Minimum: ", min(array_temp))
        print("Minimum: ", max(array_temp))
        print("Range: ", rango)
        print("Standard deviation: ", stat.stdev(array_temp))
    
    def detect_outlier(self,dataset):
        '''
        This function calculates the interquartile range (IQR), which tells if a value is too far from the middle,
        if a value is more than 1.5 times the IQR above the third quartile or below the first quartile it is considered an outlier
        '''
        outliers=[]
        sorted(dataset)
        q1, q3= np.percentile(dataset,[25,75])
        iqr = q3 - q1
        lower_bound = q1 -(1.5 * iqr) 
        upper_bound = q3 +(1.5 * iqr) 
        for y in dataset:
            if y < lower_bound or y > upper_bound:
                outliers.append(y)
        return outliers

    
    def q_getOutliers(self):
        '''
        Print the measures of an array. 
        '''
        array_temp = self.read_array()
        outlier_datapoints = self.detect_outlier(array_temp)
        if outlier_datapoints:
            print(outlier_datapoints)
        else:
            print("No outliers")
    
    def q_removeOutliers(self):
        '''
        Print the measures of an array. 
        '''
        array_temp = []
        self.pointer_stack[-1] += 1
        quadruple = self.quadruples[self.pointer_stack[-1]]
        base_address = quadruple.left
        size = quadruple.left + quadruple.right

        for x in range(base_address,size+1):
            temp = self.memory.read(x)
            if(temp is not None):
                array_temp.append(temp)
                
        outlier_datapoints = self.detect_outlier(array_temp)
        for x in array_temp:
            if x in outlier_datapoints:
                x_address = base_address + array_temp.index(x)
                array_temp[array_temp.index(x)] = None
                self.memory.write(x_address,None)
        print(array_temp)

    def q_replaceValue(self, valToReplace, replacement):
        '''
        Print the measures of an array. 
        '''
        array_temp = []
        self.pointer_stack[-1] += 1
        quadruple = self.quadruples[self.pointer_stack[-1]]
        base_address = quadruple.left
        size = quadruple.left + quadruple.right

        for x in range(base_address,size+1):
            temp = self.memory.read(x)
            if(temp is not None):
                array_temp.append(temp)
                
        for x in array_temp:
            if x == valToReplace:
                x_address = base_address + array_temp.index(x)
                array_temp[array_temp.index(x)] = replacement
                self.memory.write(x_address,replacement)
        print(array_temp)
