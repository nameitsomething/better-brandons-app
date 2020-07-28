
from socket import *
import struct
from server.Utils.Student import Student
from server.Utils.Course import Course



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

print("sent info")

data = sock.recv(128).decode().split(',')

print("recv info")

for i in range(int(data[0])):
    temp = sock.recv(1048).decode().split(',')
    
    bruh_the_first.append(Student(temp[0],temp[1],temp[2],temp[3]))
    print(temp)
    print("added student loop")

for i in range(int(data[1])):
    temp = sock.recv(2048).decode().split(',')
    bruh_the_second.append(Course(temp[0],temp[1],temp[2],temp[3]))
    print(temp)
    print("added course loop")
    




sock.sendall(str.encode(f"{66}"))




  

