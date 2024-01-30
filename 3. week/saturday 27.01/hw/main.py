check_is_balanced = '()((())('


def is_balanced(string: str) -> bool: 
    if string[0] == ')' or len(string) % 2 != 0: 
        return False
    open = 0
    close = 0
    for i in string:
        if i == '(':
            open += 1
        else: 
            close += 1
    return open == close


result = is_balanced(check_is_balanced)
print(result)