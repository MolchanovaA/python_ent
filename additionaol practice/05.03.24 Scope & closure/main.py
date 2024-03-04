

# print(s, 'BEFORE)
# s = 'some'


# some_f()

# def some_f():
#     print('hello')

# some_f()

#============

variable = 'a'

def variable():
    print('hello from var')

# print(variable, 'what is VARIABLE')

#============

x = 10  

def my_func():
    x = 5  
    # print("inside ", x)

my_func()
# print("outside ", x)


#==========

y = 5
# print('outside 1', y) 

def foo():
    global y
    y = 10
    # print('inside ', y)

foo() 
# print('outside 2', y) 

#============

def outer():
    x_1 = 1
    def inner():
        nonlocal x_1
        x_1 = 2
    # print("outer:", x_1)
    inner()
    # print("outer:", x_1)

outer()

#===========

foo = 1

def bar():
    if foo:
        foo = 100
    # print(foo, 'FOO')

bar()

#============

foo_1 = 1

def func_b():
    global foo_1
    foo_1 = 10
    return 
    def foo_1():
        pass

func_b()
print(foo_1)

#============

def test():
    t = 'TTT'

test()
# print(t)


#============


list_x = []

def test_list(l_x):
    # print(l_x, 'inside before')
    l_x += 'c'
    # print(l_x, 'INSIDE after')
    return l_x

test_list(list_x)
# print(list_x, 'AFTER OUTSIDE')
    
#============

list_y = []

def test_list_2(l_y):
    # print(l_y, 'INSIDE BEFORE')
    l_y = ['A']
    # print(l_y, 'INSIDE after')
    return l_y

test_list_2(list_y)
# print(list_y, 'OUTSIDE AFTER')

#============
b_x = '10000'
# print(b_x, 'OUTSIDE before')

if True: 
    # print(b_x, 'INSIDE before')
    b_x = '1'
    # print(b_x, 'INSIDE AFTER')

# print(b_x, 'outside after')

#-=======

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c = counter()
# print(c())  
# print(c())  
# print(c())  

#===========

