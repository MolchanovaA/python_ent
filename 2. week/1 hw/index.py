eq = '4x^2 +4x +    (-8) =  0'

pieces = eq.split('+')
a = int(pieces[0].replace('x^2', ''))
b = int(pieces[1].replace('x', ''))
c = int(pieces[2].split('=')[0].strip().lstrip('(').rstrip(')'))
print(a, b, c)

    
x_1 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
x_2 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
print(x_1, x_2)
