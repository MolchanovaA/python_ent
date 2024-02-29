def check_role(func):
    def wrapper(*args, **kwargs):
        print(args, 'ARGS')
        print(kwargs, 'KWARGS')
        func(*args, **kwargs)
    return wrapper


user = 'user'
user_info = {'name':'Olia', 'age': 20}

@check_role
def for_admin(a, **kwargs):
    print('hello admin')

for_admin(user, user_info = 'TEST')
