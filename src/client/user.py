
from socket import *
import struct



HOST  = '3.128.156.248'
PORT = 12346

user = 'user123'
pw = '12346'
info = f"{user},{pw}"
command = 2
person = "chicken"


sock = socket()


sock.connect((HOST,PORT)) #connects to server
data = sock.recv(2)
sock.sendall(str.encode(info)) #sends username and password

print("Logged on")

info = f"{command},{person}"
temp = str.encode(info)

sock.sendall(temp)

data = sock.recv(128).decode()
print(data)

sock.sendall(str.encode(f"{100}"))




  

