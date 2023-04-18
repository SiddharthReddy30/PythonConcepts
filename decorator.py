#decorator
#decorator decorates a function
#it takes function defination as a input
import logging
import math
from functools import wraps
logging.basicConfig(filename='closure.log', level=logging.INFO)

def logger(argFunc):
    @wraps(argFunc)
    def logFunc(args):
        print(f'argFunc = {argFunc.__name__}')
        logging.info(f'Running Funcion: {argFunc.__name__} with Arguments: {args} Success: \'True\' Error: \'True\'')
        return argFunc(args)
    return logFunc
#decorator
@logger
def add(args):
    return math.fsum(args)

print(f'add = {add.__name__}')
nums = (2,3,5)
print(f'sum = {add(nums)}')