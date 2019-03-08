from socket import *
host='localhost'
port=12340
import math as mt
import random
import sympy
s=socket(AF_INET,SOCK_STREAM)
s.connect((host,port))


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
print("client public key",public_key)
print("client private key",private_key)

option = s.recv(1024)  #option is send from
option=int(option)
s.send(str(us).encode())#sending client public key
s_pu=s.recv(1024)
s.send(str(n).encode())#sending N
#recieve server keys now
s_n=s.recv(1024)

s_pu=int(s_pu.decode())
s_n=int(s_n.decode())



def cipher(message):

    cipher_text = []
    cipherfin=[]

    for i in message:
        cipher_text.append(ord(i))
    for i in cipher_text:
        if option==1:
            c = pow(i,s_pu) % s_n
        elif option==2:
            c = pow(i,rs) % n
        elif option==3:
            c=pow(i,rs)%n
            if c>s_n:
                c=i
            c=pow(c,s_pu)%s_n





        cipherfin.append(str(c))
    cipherfin=' '.join(cipherfin)
    return cipherfin


def decipher(message):

        strmess = []
        mesde =message.split(' ')


        for j in mesde:
            if option==1:
                p = pow(int(j),rs) % n
            if option==2:
                p=pow(int(j),s_pu)%s_n
            if option==3:
                p=pow(int(j),rs)%n
                if(p not in range(32,127)):
                    p=pow(p,s_pu)%s_n


            strmess.append(chr(p))
        strmess = ''.join(strmess)
        return strmess



f=True
while f:

    message = str(input("Your Message: "))

    message=cipher(message)

    s.send(message.encode())
    print("Awaiting reply from server")
    reply = s.recv(1024)  # 1024 is max data that can be received
    print("***encrypted message***")
    print (reply.decode())

    decrepl=decipher(str(reply.decode()))

    print("***decrypted message***")
    print(decrepl)
    if decrepl=="bye":
        reply = cipher('bye')
        break

s.close()
