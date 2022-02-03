import os
import requests
import json

# API base url
base_url = 'http://localhost:5000/api'

# Get token
endpoint = os.path.join(base_url, 'token/user')
params = {
    "password": "root",
    "username": "root"
}
r = requests.post(endpoint, json=params)
r = r.json()
key = r['access_token']
headers = {'Authorization': 'Bearer %s' % key}

# Get keys
endpoint = os.path.join(base_url, 'node')
r = requests.get(endpoint, headers=headers)
nodes = r.json()
print(json.dumps(nodes, indent=4))