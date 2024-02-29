from flask import Flask
import json


app = Flask(__name__)
counter = 0

@app.route('/count-requests')
def count_requests():
    global counter
    counter += 1
    print(counter)
    resp = json.dumps(counter, indent=1)
    return resp


@app.route('/reset-counter', methods = ['POST'])
def reset_requests():
    global counter
    counter = 0
    resp = json.dumps(counter, indent=1)
    return resp

if __name__ == '__main__':
    app.run(debug=True)