import sys

a = sys.argv[1]
b = sys.argv[3]
toDoMath = sys.argv[2]
print(a, b, toDoMath)

def toCalculate(n, toDo, m):
    print(n , m, toDo)
    intN = int(n)
    intM = int(m)
    result = 0
    if toDo == '+':
        result = intN + intM
    elif toDo == '-':
        result = intN - intM 
    elif toDo[0] == 'C':
        result = intN / intM
    else:
        result = 'Not applicable'
    return result


res = toCalculate(a,toDoMath, b )
print(res)