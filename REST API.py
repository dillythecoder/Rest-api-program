import requests
import json

user = input("Link for API: ")
task = {"summary": "Take out trash", "description": "" }
resp = requests.post(user, json=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))
