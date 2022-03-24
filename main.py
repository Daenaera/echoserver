"""
import requests

url = "https://retoolapi.dev/R0qlrj/data"
x = requests.get(url)
json = x.json()
#for object in json:
#    print(object['Name'])

posta = {
    "id": 53,
    "Name": "Francesco",
    "Email": "astopard27@dsdev.cn",
    "Place": "Catania,Sicilia,Italy"
  }
prova = requests.post(url, data = posta)
print(prova.text)
"""


import socket

HOST = "127.0.8.1"
PORT = 65431


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)