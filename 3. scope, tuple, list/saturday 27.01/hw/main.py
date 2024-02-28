check_is_balanced = '()(())'

def is_balanced(string: str) -> bool: 
    if string[0] == ')' or string[-1] == '(' or len(string) % 2 != 0: 
        return False
    new_list = list(string)

    for x in range(len(new_list)):
        if new_list[x] == '(':
            new_list[x] = '*'
            next = new_list[x:].index(')')
            if next != (-1):
                new_list[next+x] = '*'
    res = ''
    try:
        res = new_list.index(')') or new_list.index('(')
    except ValueError: 
        res = -1
    return res <= -1



result = is_balanced(check_is_balanced)
print(result)