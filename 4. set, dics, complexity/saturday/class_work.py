print('hello')


def dif(a, b): 
    c = [x for x in a if x in b]
    print(c)


one = ['a', 'b', 'c']
two = ['v', 'a', 'c', 'r']

dif(one, two)