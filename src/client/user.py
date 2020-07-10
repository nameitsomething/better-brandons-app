
from socket import *



HOST  = '3.128.156.248'
PORT = 12346

user = 'user123'
pw = '12346'
info = f"{user},{pw}"
command = 2
person = 'ulanda'


sock = socket()


sock.connect((HOST,PORT)) #connects to server
sock.sendall(str.encode(info)) #sends username and password

print("Logged on")

info = f"{command},{person}" 
sock.sendall(str.encode(info))

data = sock.recv(128)
print(data)




  

