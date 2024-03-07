from flask import Flask, request
import json
from report import db_reader_prog_report_creator


app = Flask(__name__)

@app.route('/birthdays')
def get_data():
    params = request.args
    request_dict = {}
    for value in params:
        request_dict[value] = params[value]

    report = db_reader_prog_report_creator(request_dict['month'], request_dict['department'])

    return json.dumps(report , indent=1)



if __name__ == '__main__':
    app.run(debug=True)