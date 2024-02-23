print('hi')
# Problem 2: Word Counter

# Write a Python program that takes a filename as input and counts the number of
# occurences for each word in the file. Write the word stats to a new file.

# TODO:
import json

def count_words(file_name):
    counter_dict = {}
    with open(f'{file_name}.txt', 'r') as file:
        text = file.read()
    array_of_words = text.lower().split()
    for word in array_of_words:
        word = word if word[-1].isalpha() else word[:-1]
        counter_dict[word] = counter_dict.get(word, 0) + 1
    return counter_dict


def file_writter(info):
    with open('new_file.json', 'w') as file:
        json.dump(info, file, indent=1)


if __name__ == '__main__':   
    name = input('type file name  ')
    counter_d = count_words(name)
    file_writter(counter_d)