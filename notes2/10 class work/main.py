print('hhh')


from bs4 import BeautifulSoup
import requests
import math
import numpy as np

# url = 'https://gutenberg.org/cache/epub/1342/pg1342-images.html'
# response = requests.get(url)


# soup = BeautifulSoup(response.text, 'html.parser')
# from collections import Counter 
# text = soup.get_text().replace('\n', ' ').replace('\r', ' ')
# text = text.lower() 
# text = text.split() 
# word_counts = Counter(text) 

# word = ''
# max = 0

# for w in word_counts:
#     if 'jane' == w:
#         max = word_counts[w]
#         # word = w

# print(word_counts['jane'], 'JANE' )


# def add_numbers(a, b):
#     return a + b

# def calculate_sum_of_list(numbers):
#     return sum(numbers)
#     # total = 0
#     # for num in numbers:
#     #     total = add_numbers(total, num)
#     # return total


# t = calculate_sum_of_list([1,2,3,4])
# print(t)



# def f_(x):
#     return (2/math.pi)*(x/math.pi - math.floor(x/math.pi + 1/2))

# list_x = np.arange(10)
# print(list_x)



# import matplotlib.pyplot as plt

# def f(x):
#     return (2 / np.pi) * (x / np.pi - np.floor(x / np.pi + 0.5))




###

# x_values = np.linspace(0, 10, )
# y_values = f(x_values)


# plt.plot(x_values, y_values, label=r"$f(x) = \frac{2}{\pi} \left(\frac{x}{\pi} - \lfloor \frac{x}{\pi} + \frac{1}{2} \rfloor\right)$")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("Графік функції f(x)")
# plt.grid(True)
# plt.legend()
# plt.show()


with open('random_list.txt') as f:
    