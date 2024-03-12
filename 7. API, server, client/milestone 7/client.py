import requests
from report import report_printer

def get_report():
    month = 'march'
    department = 'admin'
    URL = f'http://127.0.0.1:5000/birthdays?month={month}&department={department}'
    # print(URL)
    response = requests.get(URL)
    response_json = response.json()
    formatted = report_printer(response_json, month)
    # print(response_json)
    return formatted

get_report()

def get_repository_info(repo_name: str):
    GITHUB_URL = f'https://api.github.com/repos/{repo_name}'
    resp_github = requests.get(GITHUB_URL)
    response_json = resp_github.json()
    result = {'repo_name': response_json['name'], 'owner': response_json['owner']['login'], 
              'description':response_json['description'], 'created': response_json['created_at'], }
    if response_json.get('license'):
        result['license'] = response_json['license']
    print(result)
    return result
        

# get_repository_info("octocat/Hello-World")