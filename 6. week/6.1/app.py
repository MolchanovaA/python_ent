import sys

a = sys.argv[1]
b = sys.argv[3]
toDoMath = sys.argv[2]
if b[0] == 'a':
    l = len(sys.argv) - 1
    b = sys.argv[l]
    toDoMath = '*'
print(a, b, toDoMath, 'INPUT')
print(sys.argv)

def toCalculate(n, toDo, m):
    intN = int(n)
    intM = int(m)
    result = 0
    if toDo == '+':
        result = intN + intM
    elif toDo == '-':
        result = intN - intM 
    elif toDo == '*':
        result = intM * intN
    else:
        result = 'Not applicable'
    return result

res = toCalculate(a,toDoMath, b )
print(res)