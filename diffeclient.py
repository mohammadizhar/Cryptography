from random import *
from socket import *
host='localhost'
port=8888
s=socket(AF_INET,SOCK_STREAM)
s.connect((host,port))
q=s.recv(1024)
q=int(q.decode())

print("Recieved q:",q)
alp=s.recv(1024)
alp=int(alp.decode())
print("Recived Alpha value:",alp)
xb=randrange(3,q)
yb=pow(alp,xb,q)
print("yb choseen:",yb)
s.send(str(yb).encode())
ya=s.recv(1024)
ya=int(ya.decode())
print("value of ya recieved:",ya)
kb=pow(ya,xb)%q

print("key generated at client side is:",kb)
s.close()








