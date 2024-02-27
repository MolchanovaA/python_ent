import sys

a = sys.argv[1]
b = sys.argv[2]
toDoMath = sys.argv[3]

def toCalculate(n , m , toDo):
    intN = int(n)
    intM = int(m)
    result = 0
    if toDo == '+':
        result = intN + intM
    elif toDo == '-':
        result = intN - intM 
    else:
        result = 'Not applicable'
    return result


res = toCalculate(a, b, toDoMath)
print(res)