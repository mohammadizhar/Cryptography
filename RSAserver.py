from socket import *
host='localhost'
port=12340
import math as mt
import random
import sympy
#network part chat
s=socket(AF_INET,SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
print("Connected by ",addr)


def mulinv(r1, r2):
    tr1 = r1
    t1 = 0
    t2 = 1
    l = []
    tg = []
    t2a = []
    while r1 > r2 and r1 > 1:
        q = r1 // r2
        t = t1 - (q * t2)
        l.append(q)
        tg.append(t)
        t2a.append(t2)
        r = r1 % r2
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t
    m = t2a.pop()
    if (m < 0):
        m += tr1

    return (m)


def keygen():
    pq = []
    poe = []
    pq.append(sympy.randprime(10, 900))
    pq.append(sympy.randprime(10, 900))
    pa = pq[0]
    qa = pq[1]
    print(pq)
    tf = pa * qa
    sm = (pa - 1) * (qa - 1)
    for i in range(sm - 1, 2, -3000):
        if (mt.gcd(i, sm) == 1):
            poe.append(i)
    pu = random.choice(poe)  # this is the public key"""

    pr = mulinv(sm, pu)
    return tf, pu, pr;





n,us,rs=keygen()
public_key=[us,n]
private_key=[rs,n]
print("server public key",public_key)
print("server private key",private_key)
print("please enter your option \npress 1 for encryption \n press 2 for digital sign\n press 3 for both")
o=int(input("Enter your choice:"))


ms=str(o)
conn.sendall(ms.encode())#option sending to client
data=conn.recv(1024)#client public key

cl_pu=data.decode()
ms=str(us)
conn.sendall(ms.encode())
cl_pu=int(cl_pu)
data=conn.recv(1024)#client N
cn=data.decode()
cl_n=int(cn)
#now sending servers key
ms=str(n)
conn.sendall(ms.encode())
print("client public key")
print(cl_pu)
print(cl_n)
def cipher1(message):

    cipher_text = []
    cipherfin=[]

    for i in message:
        cipher_text.append(ord(i))
    for i in cipher_text:
        c = pow(i,rs) % n
        if c>cl_n:
            c=i
        cipherfin.append(c)
    print(cipherfin)

    return cipherfin
def cipher2(ilt):
    cipher_text=[]
    for i in ilt:


        c = pow(i,cl_pu) % cl_n
        cipher_text.append(str(c))
    cipher_text=' '.join(cipher_text)
    return cipher_text
#########


def cipher(message):


    cipher_text = []
    cipherfin=[]

    for i in message:
        cipher_text.append(ord(i))
    for i in cipher_text:
        if o==1:
            c = pow(i,cl_pu) % cl_n
        elif o==2:
            c = pow(i,rs) % n
        elif o==3:
            c=pow(i,rs)%n
            if c>cl_n:
                c=i
            c=pow(c,cl_pu)%cl_n


        cipherfin.append(str(c))
    cipherfin=' '.join(cipherfin)
    return cipherfin



def decipher(message):


    strmess = []
    mesde =message.split(' ')


    for j in mesde:
        if o==1:
            p = pow(int(j),rs) % n
        elif o==2:
            try:
                p=pow(int(j),cl_pu)%cl_n
            except ValueError:
                pass
        elif o == 3:
            p = pow(int(j), rs) % n
            if (p not in range(32, 127)):
                p = pow(p, cl_pu) % cl_n



        strmess.append(chr(p))
    strmess = ''.join(strmess)
    return strmess



f=True
while f:
    print("Waiting for client response")
    data = str((conn.recv(2048)).decode())
    print("***encrypted message***")
    print(data)

    decr=decipher(data)


    print("***decrypted****")
    print(decr)

    reply = str(input("Enter your reply:"))

    repl = cipher(reply)


    conn.sendall(repl.encode())
    if decr=='bye':
        reply=cipher('bye')
        conn.sendall(reply.encode())
        break
conn.close()

