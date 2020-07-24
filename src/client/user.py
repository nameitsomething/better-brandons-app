
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

class Student:
    def __init__(self,name,age:int,grade:int,present:bool, number:int):
        self.name = name
        self.age = age
        self.grade = grade
        self.present = present
        self.sutdent_number = number
    

sock.connect((HOST,PORT)) #connects to server
data = sock.recv(2)
sock.sendall(str.encode(info)) #sends username and password

print("Logged on")

info = f"{command}"
temp = str.encode(info)

sock.sendall(temp)

print("sent info")

data = sock.recv(128).decode().split(',')

print("recv info")

for i in range(int(data[0])):
    temp = sock.recv(1048).decode()
    bruh_the_first.append(temp)
    print(temp)
    print("added student loop")

for i in range(int(data[1])):
    temp = sock.recv(2048).decode()
    bruh_the_second.append(temp)
    print(temp)
    print("added course loop")
    




sock.sendall(str.encode(f"{66}"))




  

