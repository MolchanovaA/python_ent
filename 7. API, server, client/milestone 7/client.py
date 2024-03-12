import requests
import sys
from report import report_printer


def get_report(month, department):
   
    URL = f'http://127.0.0.1:5000/birthdays?month={month}&department={department}'

    response = requests.get(URL)
    response_json = response.json()
    formatted = report_printer(response_json, month)
    print(response_json)
    return formatted

month_to_check = sys.argv[1]
dpt_to_check = sys.argv[2]

get_report(month_to_check, dpt_to_check)


        

