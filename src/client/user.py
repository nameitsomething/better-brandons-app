
from socket import *



HOST  = '3.128.156.248'
PORT = 12346

user = 'user123'
pw = '12346'
info = f"{user},{pw}"

sock = socket()

sock.connect((HOST,PORT)) #connects to server
sock.sendall(str.encode(info)) #sends username and password

sock.sendall((2,'ulanda').encode())

data = sock.recv(128)
print(data)




  

