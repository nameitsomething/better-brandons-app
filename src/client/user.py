from tkinter import *
from socket import *
from struct import *


HOST  = '3.128.156.248'
PORT = 12346

user = 'user123'
pw = '12346'
info = f"{user},{pw}"


sock.connect((HOST,PORT))
sock.sendall(info.encode())

sock.sendall(struct.pack("B",2))

data = sock.recv(data.decode())



  

