
# start = 12345
# counter = 0

# while start != 1:
# # for i in range(start):
#     counter += 1
#     if start % 2 == 0:
#         start = start//2 
#     elif start % 2 != 0:
#         start = start * 3 + 1

# print(counter, 'for i ')
# print('hello')

# Sum of Digits

# Write a program that takes an integer as input and calculates the sum of its digits.

# For example, if the input is 1234, the output should be 10.

# number = input('add number')

# res = 0

# for dig in number:
#     res += int(dig)
# print(res, 'result')

# print(26//10) => 2
# print(26%10) => 6

# number = '12345'

# res = 0
# i = len(number)

# while i > 0:
#     int_num = int(number)
#     res += int_num % 10
#     number = number[0:-1]
#     i -= 1
# print(res)


def is_prime(num):
    if num <= 3:
        print(f'number {num} is Prime')
        return True
    if num % 2 == 0 or num % 3 == 0:
        print(f'number {num} is NOT Prime')
        return False
    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            print(f'number {num} is NOT Prime')
            return False
        i += 6

    print(f'number {num} is Prime')
    return True

# is_prime(53)


even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)
