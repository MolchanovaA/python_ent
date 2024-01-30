alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 1
msg_to_decrypt = 'Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.'
correct_msg = ''

for i in msg_to_decrypt:
    char = alphabet.find(i.lower())
    capitalized = False
    secret_char = ''
    if i == i.upper() and char != (-1):
        capitalized = True
    if char == (-1):
        secret_char = str(i)
    else: 
        secret_num = alphabet.find(i.lower()) - key
        if secret_num >= 26: 
            secret_num = secret_num % 26
        if capitalized: 
            secret_char = alphabet[secret_num].upper()
        else: 
            secret_char = alphabet[secret_num]
    correct_msg += secret_char

print(correct_msg)