from flask import Flask, request
import csv
import json

from modules import get_info_from_db as getter

#?author=Jack London
app = Flask(__name__)



@app.route('/books', methods = ['GET', 'POST'])
def read_books():
    params = request.args
    key = ''
    value = ''
    for entries in params:
        key = entries
        value = params[entries].replace('_', ' ')
        
    
    result = getter(key, value)
    return result

print('SERVER START')
if __name__ == '__main__': 
    app.run(debug=True)
