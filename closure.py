#closures
#closure takes anything as an argument, spits out a function based on the arguments passed,that is generaged to server a purpose based on the arguments passed. 
import logging     
import math
logging.basicConfig(filename='closure.log', level=logging.INFO)

def add(args):
    return math.fsum(args)

def logger(argFunc):
    def logFunc(args):
        print(f'argFunc = {argFunc.__name__}')
        logging.info(f'Running Funcion: {argFunc.__name__} with Arguments: {args} Success: \'True\' Error: \'True\'')
        return argFunc(args)
    return logFunc

#closure
add_logger = logger(add)

print(f'add_logger = {add_logger.__name__}')
nums = (2,3,4)
print(f'SUM ={add_logger(nums)}')