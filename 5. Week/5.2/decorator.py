def make_bold(func):
    def decor(*args, **kwargs):
        return f"***" + func(*args, **kwargs) + f" **"
    return decor


def make_italic(func):
    def decor(*args, **kwargs):
        return f'__' + func(*args, **kwargs) + '__'
    return decor


@make_italic
@make_bold
def hello(name):
    return f'Hello, {name}'


greetings = hello('Ivan')

# print(greetings, 'RESULT')

def repeat(times):
    def wraper_repeat(func):
        def inner(*args, **kwargs):
            for _ in range(times): 
                value = func(*args, **kwargs)
            return value
        return inner
    return wraper_repeat

@repeat(times=5)
def hello_repeat(name):
    # print('REPEATING')
    return f'Hello several times to {name}'


greetings_repeat = hello_repeat('Mike')
# print(greetings_repeat, 'Res 2')



# ============= TASKS FROM LESSON 5.2 ================

# TASK 1.
# Write a decorator that will calculate the execution time of a function.
from datetime import datetime


def calculate_time(func):
    def wrapper(*args, **kwargs):
            start = datetime.now()
            func(*args, **kwargs)
            end = datetime.now()
            total_time = end-start
            print(total_time.total_seconds())
    
    return wrapper
    
@calculate_time
def hello_3():
    print('hello_invoked')
    list = 0
    for _ in range(10_000_000):
        list += _
    print('hello finished')


# hello_3()
    
# Task 2. 
# Write a decorator that ensures a function is only called by users 
# with a specific role. Each function should have an user_type with a string type in kwargs
    
def is_admin(func):
    def inner(*args, **kwargs):
        # print(args, kwargs)
        if kwargs['user'] == 'admin':
            func(*args, **kwargs)
        else:
            raise ValueError('USER is NOT ADMIN')
    return inner
    


    
@is_admin
def show_rights(user: 'user'):
    print('invoked', user)

# show_rights(user ='admin')
    

# Task 3. 
# Write a decorator that wraps a function in a try-except block
# and print an error if any error has happened
    
def catch_error(func):
    def wrapper(*args, **kwargs):
        list_of_args = list(args[0].items())
        for key, value in list_of_args: 
            try:
                return func(*args, **kwargs)
            except Exception:
                print(f'no KEY as {key}')
                
    return wrapper


@catch_error
def list_3(data):
    print(data['key_1'], 'RESULT')
   

test_data = {'key_1': 'value_2'}
test_data_2 = {'foo': 'bar'}
# list_3(test_data)
# list_3(test_data_2)


# Task 4. 
# Optional: Create a decorator that will check types.
# It should take a function with arguments and validate inputs with annotations.

def check_types(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as error_info:
            # print(args, 'ARGS')
            # errors = []
            for i in args:
                if type(i) == str:
                    print(f'TypeError: Argument {i} must be int, not str')
                elif type(i) == bool: 
                    print(f'TypeError: Argument {i} must be int, not bool')

    
    return wrapper

@check_types
def add(a, b):
    print(a + b)

# add(2, '3', 'l', True, None)
    

# Task 5. 
# Optional: Create a function that caches the result of a function, 
# so that if it is called with same same argument multiple times, 
# it returns the cached result first instead of re-executing the function. 
# It`s one of the real task on the project

def cache(func):
    cached_args = ['zero']
    cached_result = []

    def wraper(*args, **kwargs):
        if cached_args[0] == args[0]: 
            return cached_result[0]
        else:
            cached_args.append(args)
            result = func(*args, **kwargs)
            cached_result.append(result)
            return result
    return wraper


@cache
def add_chache(a):
    print('add func called')
    return a + 10


# eleven = add_chache(1)
# print(eleven)
# print(eleven)
# print(eleven)

# fifteen = add_chache(5)
# print(fifteen)
# print(fifteen)


# Task 6. 
#  Optional: Write a decorator that adds a rate-limiter to a function,
#  so that it can only be called a certain amount of times per minute.

def time_limiter(limit: int):
    counter = {'limit_to_envoke': limit}

    time_cache = {
        'start': None,
        'end': None,
        'passed': None
    }
    

    def decorator(func):

        def inner(*args, **kwargs): 
            if time_cache['start'] is None:
                time_cache['start'] = datetime.now().timestamp()
           

            counter['limit_to_envoke'] -= 1
            if counter['limit_to_envoke'] < 0 and time_cache['passed'] < 10: 
                print('LIMIT EXCEEDED')
            else: 
                func(*args, **kwargs)
                end = datetime.now().timestamp()
                time_cache['passed'] = end - time_cache['start']

  
        return inner

    return decorator
     


@time_limiter(2) # limit: 2 times per 10 sec
def printer(word): 
    sum = 0
    for _ in range(100_000_000): 
        sum += _
    print(f'This is {word}')


printer('SPARTA')
printer('SPARTA_1')
printer('SPARTA_2')
# printer('SPARTA')
# printer('SPARTA')
# printer('SPARTA')