import requests
import json


# data = {'account': 'wanyl', 'password': '112233'}
# r = requests.post("http://192.168.0.54:8000/login/", data=data)
# r = requests.get("http://127.0.0.1:8000/interfaces/")


# data = json.dumps({'username': 'admin', 'password': 'admin'})
# r = requests.post("http://127.0.0.1:8000/user/login/", data=data)

# data = {'token': '123','admin': 'admin'}
# r = requests.get("http://127.0.0.1:8000/user/info/", params=data)

# params = {'id': 'all'}
# r = requests.get("http://127.0.0.1:8000/show/UiTestCases/", params=params)


# data = json.dumps({'id': '5', 'describe': '2131', 'caseName': '万达单', 'beginSteps': '', 'steps': '', 'endSteps': '123',
#                    'owner': 'wanyl', 'showToAll': True, 'project': '', 'platform': ''})
# r = requests.post("http://127.0.0.1:8000/update/UiTestCases/", data=data)

# data = json.dumps({'id': '5', 'describe': '231', })
# r = requests.post("http://127.0.0.1:8000/update/UiTestCasesSet/", data=data)


# params = {'id': 'all'}
# r = requests.get("http://127.0.0.1:8000/show/UiTestCasesSet/", params=params)


print(r.json())
print(r.status_code)
