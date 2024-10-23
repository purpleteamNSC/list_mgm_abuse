import requests


def add(n, id_lista="1234"):
    url = "http://127.0.0.1:5000/ip"
    # data = {
    #     'ip': f'192.168.0.{n}',
    #     '':'',
    #     '':''
    #     }

    payload = {
        "value": f"192.168.0.{n}",
        "type": "ipv4",
        "risk": "Low",
        "notes": "secdevops",
        "list": f"{id_lista}",
    }
    response = requests.post(url, json=payload)
    print(response.json())


t = 1
while t != 255:
    add(t)
    t += 1
