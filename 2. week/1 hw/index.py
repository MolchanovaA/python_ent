# eq = 'x^2 -7x +12 =  0'
eq = input('type quadratic equations in correct order: `<a>x^2 + <b>x + <c> = 0` \n')
eq = eq.replace(' ', '')

a_sign = '+'
a = 1
b_sign = '+'
b = 1
c_sign = '+'
c = 0

a = eq.split('x^2')[0]
a_sign = '-' if '-' in a else '+'
if a_sign == '-': 
    try:
        a = int(a[1:])
    except ValueError:
        a = 1

try:
    a = int(a)
except ValueError:
    a = 1

a = int(a)*(-1) if a_sign == '-' else int(a)

without_a = eq.split('x^2')[1]
b = without_a.split('x')[0]

if '(' in b:
    sign_before_apr = b.split('(')[0]
    sign_after_apr = b.split('(')[1][0:1]
    b_sign = '-' if sign_before_apr != sign_after_apr else '+'
    b = int(b.split('(')[1][1:] or 1)
else:
    try:
        b = int(b)
    except ValueError:
        b = 1

b = int(b*(-1)) if b_sign == '-' else int(b)

without_a_b = without_a.split('x')[1]
apr_cl = without_a_b.split('=')[0]

without_a_b_equ = apr_cl if ')' not in apr_cl[0:1] else apr_cl.strip(')')
c_sign = without_a_b_equ[0:1]


if '(' in without_a_b_equ: 
    c = without_a_b_equ.split('(')[1]
    if c[0:1] == '-' and c_sign == '-': 
        c_sign = '+'
    elif c[0:1] == '-' and c_sign == '+': 
        c_sign = '-'
    c = c.rstrip(')')[1:]
else: 
    c = without_a_b_equ[1:]

c = int(c)*(-1) if c_sign == '-' else int(c)

# print(a)
# print(b)
# print(c)

x_1 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
x_2 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
print(x_1, x_2, 'result')

