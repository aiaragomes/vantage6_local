import os
import requests

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

# Add organizations
endpoint = os.path.join(base_url, 'organization')
params = {
    'name': 'Maastro',
    'address1': 'Dr Tanslaan 12',
    'address2': '',
    'zipcode': '6229 ET',
    'country': 'The Netherlands',
    'domain': 'https://maastro.nl/',
    'roles': [3]
}
r = requests.post(endpoint, headers=headers, json=params)
params = {
    'name': 'Hospital',
    'address1': 'Street 1',
    'address2': '',
    'zipcode': '1234 AB',
    'country': 'The Netherlands',
    'domain': '',
    'roles': [3]
}
r = requests.post(endpoint, headers=headers, json=params)
r = requests.get(endpoint, headers=headers)
orgs = r.json()

# Add collaborations
endpoint = os.path.join(base_url, 'collaboration')
params = {
    'name': 'Project',
    'organization_ids': [2, 3], # check which ids were assigned to the orgs
    'encrypted': False,
    'tasks': ['testing']
}
r = requests.post(endpoint, headers=headers, json=params)
r = requests.get(endpoint, headers=headers)
colabs = r.json()

# Add users
endpoint = os.path.join(base_url, 'user')
params = {
    'username': 'leia',
    'firstname': 'Leia',
    'lastname': 'Skywalker',
    'password': '12345',
    'email': 'leia@skywalker',
    'organization_id': 2,
    'roles': '3',
    'rules': '3'
}
r = requests.post(endpoint, headers=headers, json=params)
r = requests.get(endpoint, headers=headers)
users = r.json()

# Add nodes (adding a node will create a token that can be used later)
endpoint = os.path.join(base_url, 'node')
params = {
    'collaboration_id': 1,
    'organization_id': 2
}
r = requests.post(endpoint, headers=headers, json=params)
params = {
    'collaboration_id': 1,
    'organization_id': 3
}
r = requests.post(endpoint, headers=headers, json=params)
r = requests.get(endpoint, headers=headers)
nodes = r.json()
