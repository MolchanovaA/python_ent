

# print(s, 'BEFORE)
      
# s = 'some'


# some_f()

# def some_f():
#     print('hello')

# some_f()

#============

# variable = 'a'

# def variable():
#     print('hello from var')

# variable = 'l'

# print(variable, 'what is VARIABLE')

#============

# x = 10  

# def my_func():
#     global x
#     x = 5  
#     print("inside ", x)
#     # return x

# my_func()
# print("outside ", x)


#==========

# y = 5
# print('outside 1', y) 

# def foo():
#     global y
#     y = 10
#     print('inside ', y)

# foo() 
# print('outside 2', y) 

#============

# def outer():
#     x_1 = 1
#     def inner():
#         nonlocal x_1
#         x_1 = 2

#     print("outer: BEFORE", x_1)
#     inner()
#     print("outer: AFTER", x_1)

# outer()

#===========

# foo = ['a', 'b']

# def bar():
#     global foo
#     some = foo
#     print(some, 'SOME')
#     # some = '999'
#     some.append('hhh')
#     some += ['K']
#     if some:
#         print(some, foo, 'SOME + FOO')
#         foo = 100
#         # print(foo, 'FOO INSIDE')

# bar()
# print(foo, 'AFTER')

#============

# foo_1 = 1

# def func_b():
#     # global foo_1
#     foo_1 = 10
#     foo_1 = 888
#     # return 
#     def foo_1():
#         pass
#     print(type(foo_1))

# func_b()
# print(foo_1)

#============

def test():
    t = 'TTT'

# test()
# print(t)


#============


# list_x = []

# def test_list(l_x):
#     print(l_x, 'inside before')
#     l_x += 'c'
#     # l_x.append('J')
#     print(l_x, 'INSIDE after')
#     # return l_x

# test_list(list_x)
# print(list_x, 'AFTER OUTSIDE')
    
#============

# list_y = []
# print(id(list_y), 'BEFORE OUTSIDE')

# def test_list_2(l_y):
#     print(id(l_y), 'INSIDE BEFORE')
#     l_y = ['A']
#     print(id(l_y), 'INSIDE')
#     # print(l_y, 'INSIDE after')
#     # return l_y

# test_list_2(list_y)
# print(id(list_y), 'BEFORE OUTSIDE')
# print(list_y, 'OUTSIDE AFTER')

#============
# b_x = 10000
# print(id(b_x), 'OUTSIDE before')

# if True: 
#     # print(b_x, 'INSIDE before')
#     b_x += 1
#     print(id(b_x), 'INSIDE AFTER')

# print(id(b_x), 'outside after')

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


def outside():
    x = 0
    def wrapper():
        nonlocal x 
        x += 1
        return x
    
    return wrapper

t = outside()
o = t()
two = t()
three = t()
four = t()
five = t()

print(o, two, three, four, five,  'VAR T')

p = outside()
op = p()
op_two = p()
op_three = p()

print(op,op_two,op_three, 'OP'  )
