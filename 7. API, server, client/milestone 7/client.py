import requests
from report import report_printer

def get_report():
    month = 'march'
    department = 'admin'
    URL = f'http://127.0.0.1:5000/birthdays?month={month}&department={department}'
    response = requests.get(URL)
    response_json = response.json()
    formatted = report_printer(response_json, month)
    print(formatted)
    return formatted

get_report()