
from socket import *
import struct



HOST  = '3.128.156.248'
PORT = 12346

user = 'user123'
pw = '12346'
info = f"{user},{pw}"
command = 24
person = "chicken"

bruh_the_first = []
bruh_the_second = []


sock = socket()


sock.connect((HOST,PORT)) #connects to server
data = sock.recv(2)
sock.sendall(str.encode(info)) #sends username and password

print("Logged on")

info = f"{command}"
temp = str.encode(info)

sock.sendall(temp)

data = sock.recv(128).decode().split(',')

for i in range(data[0]):
    temp = sock.recv(1048).decode()
    bruh_the_first.append(temp)
    print(temp)

for i in range(data[1]):
    temp = sock.recv(2048).decode()
    bruh_the_second.append(temp)
    print(temp)
    
    

sock.sendall(str.encode(f"{66}"))




  

