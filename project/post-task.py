import requests
import json

def post(data, tag):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url='http://127.0.0.1:9052/{}'.format(tag), headers=headers, data=json.dumps(data))
    print(response)
    print(response.json())

data = {"task": "binary", "jobid": "demo"}
post(data, 'task')
