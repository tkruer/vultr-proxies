import requests
import time
from base64 import b64encode
import json
import os


def loadAccountInfo(key: str) -> str:
    headers = {
        'Authorization': f'Bearer {key}',
    }
    response = requests.get('https://api.vultr.com/v2/account', headers=headers)
    print(response.json())
    return response.json()

def createStartupScript(key: str) -> str:
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json',
    }
    f = open('src/startup.txt', 'r')
    content = str(f.read())
    base64_encoded = 'QmFzZTY0IEV4YW1wbGUgRGF0YQ=='
    # come back to this here
    json_data = {
        'name': 'Squid Proxy Startup Script',
        # double check this here
        'type': 'pxe',
        'script': f'{base64_encoded}',
    }

    response = requests.post('https://api.vultr.com/v2/startup-scripts', headers=headers, json=json_data)
    f = open('src/config.json', 'w')
    f.write(response.text)
    return response.json()

def create(key: str, location: str, proxies: str, osid: str) -> str:
    headers = {'API-Key': key}
    url = 'https://api.vultr.com/v1/'
    create_response = requests.get(url + 'startupscript/list', headers=headers)
    serverlist = []
    create_data = create_response.json()
    for subid, server in create_data.items():
        serverlist.append(server)
        scriptData = subid
    if location == 'Miami':
        locale = '39'
    elif location == 'Dallas':
        locale = '3'
    elif location == 'Seattle':
        locale = '4'
    elif location == 'Atlanta':
        locale = '6'
    elif location == 'Chicago':
        locale = '2'
    elif location == 'LA':
        locale = '5'
    elif location == 'NY':
        locale = '1'
    elif location == 'Silicon Valley':
        locale = '12'
    elif location == 'Germany':
        locale = '9'
    elif location == 'France':
        locale = '24'
    elif location == 'UK':
        locale = '8'
    elif location == 'Amsterdam':
        locale = '7'
    elif location == 'Singapore':
        locale = '40'
    elif location == 'Tokyo':
        locale = '25'
    elif location == 'Sydney':
        locale = '19'
    else:
        print('You entered an invalid location, please try again.')
    data = [
        ('DCID', locale),
        ('VPSPLANID',"201"),
        ('OSID',"160"),
        ('SCRIPTID', osid),
        ('SUBID', "test")
    ]
    for i in range(int(proxies)):
        create_server = requests.post(url + 'server/create', headers=headers, data=data)
        print(create_server.text)
        time.sleep(1)
    return "Successfully created proxies"

def server_destroy(key: str) -> str:
    return

def write_to_file(key: str) -> str:
    return

