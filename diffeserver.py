from socket import *
host='localhost'
from random import *
port=8888
import sympy
s=socket(AF_INET,SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
print("connected by client with ip:",addr)

q=sympy.randprime(100,200)
ms=str(q)
conn.sendall(ms.encode())
print("***You are at server side***")
print("generated q:",q)

def primitiveroot(al,n):
    ls=set()
    rs=set()
    for i in range(1,n):
        ls.add(i)
    for j in range(1,n):
        k=pow(al,j)%n
        rs.add(k)
    fs=ls.symmetric_difference(rs)
    if(len(fs)==0):
        return True
    else:
        return False
#code to generate primitive root array
primroo=[]
for i in range(1,q):
    if(primitiveroot(i,q)):
        primroo.append(i)

alp=choice(primroo)
#sending alpha value to client
conn.sendall(str(alp).encode())
print("alpha chossen",alp)
dat=conn.recv(1024)#recieving value of yb
dat=int(dat.decode())
print("yb value of client:",dat)


xa=randrange(3,q)
print("xa choseen:",xa)
ya=pow(alp,xa,q)
conn.sendall(str(ya).encode())

print("ya:",ya)
key_ser=pow(dat,xa)%q
print("key generated over here server side is :",key_ser)
conn.close()
