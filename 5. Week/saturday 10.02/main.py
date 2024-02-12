# obj = {'a': 1, 'b':2, 'c':3}

# keys = obj.keys()
# obj['d'] = 4
# print(len(keys), 'LEN PY')

sent = 'This is a sample text. This text is a good example.'


def word_counter(sentence): 
    result = {}
    splitted_sent = sentence.split()
    for word in splitted_sent:
        word = word.strip('.')
        if result.get(word):
            result[word] += 1
        else:
            result[word] = 1
    
    print(result)


word_counter(sent)