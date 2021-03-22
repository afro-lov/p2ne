# import paramiko
# import time

import requests, json
import pprint as pp

login = 'restapi'
password = 'j0sg1280-7@'

r = requests.post('https://10.31.70.210:55443/api/v1/auth/token-services', auth=(login,password), verify=False)
print(r.json()['token-id'])
h = {'content-type': 'application/json', 'X-Auth-Token': r.json()['token-id']}

g = requests.get('https://10.31.70.210:55443/api/v1/interfaces', headers=h, verify=False)

for a in g.json()['items']:
    # print(a)
    for k,v in a.items():
        # print(k,v)
        if k == 'if-name':
            url = 'https://10.31.70.210:55443/api/v1/interfaces/'+v+'/statistics'
            stat = requests.get(url, headers=h, verify=False)
            print(stat.json())
    

# g = requests.get('https://10.31.70.210:55443/api/v1/interfaces/interface_name/statistics', headers=h, verify=False)
