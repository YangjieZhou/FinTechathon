import requests
import json

def post(data, tag):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url='http://127.0.0.1:9052/{}'.format(tag), headers=headers, data=json.dumps(data))
    print(response.json())

for i in range(7,15):
    data = {"userid": "{}".format(i), "task": "binary"}
    post(data, 'query')

for i in range(7,15):
    data = {"userid": "{}".format(i), "task": "multi"}
    post(data, 'query')
#data = {"task": "binary", "jobid": "third_task25"}
#post(data, 'task')
