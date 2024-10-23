import requests


def add(n):
    url = 'http://127.0.0.1:5000/ip'
    data = {'ip': f'192.168.0.{n}'}
    response = requests.post(url, json=data)
    print(response.json())

t = 1
while t != 255:
    add(t)
    t+=1
