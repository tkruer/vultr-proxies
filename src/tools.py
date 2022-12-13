import requests
import json
import os

def loadscript(key: str) -> str:
    f = open('src/startup.txt', 'r')
    content = f.read()
    data = [
        ('name', 'script'),
        ('script', content),
    ]
    headers = {'API-Key': key}
    url = 'https://api.vultr.com/v1/'
    load_script = requests.post(url + 'startupscript/create', headers=headers, data=data)
    #write response to file
    f = open('src/config.json', 'w')
    f.write(load_script.text)
    return load_script.json()

def server_create(key: str) -> str:
    headers = {'API-Key': key}
    url = 'https://api.vultr.com/v1/'
    return

def server_destroy(key: str) -> str:
    return

def write_to_file(key: str) -> str:
    return

