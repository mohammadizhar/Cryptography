import math
print("Programme for product cipher substitution and transposition")
d={}
le=[]
t=[]
de=[]
for i in range(26):
    d[i] = chr(i + 65)
for i in range(26, 52):
    d[i] = chr(i + 71)
d[52] = chr(32)
def substitution():
    while True:
            print("press 1 for encipher \n  2 for decipher \n  3 for exit")
            sbc=int(input("enter your choice"))
            if sbc==1:
                sencipher()
            elif sbc==2:
                sdecipher()
            else:
                break
def transposition():
    while True:
            print("press 1 for encipher \n  2 for decipher \n  3 for exit")
            tpc=int(input("enter your choice"))
            if tpc==1:
                tencipher()
            elif tpc==2:
                tdecipher()
            else:
                break        
def sencipher():
    k=int(input("enter your key:"))
    f1=open('message.txt','r')
    inpt=f1.readline()
    f1.close()

    for i in inpt:
        if (ord(i) >= 65 and ord(i) <= 90):
            nv = ord(i) - 65
        elif (ord(i) >= 97 and ord(i) <= 122):
            nv = ord(i) - 71
        elif (ord(i) == 32):
            nv = ord(i) + 20

        else:
            print("unacceptable symbol allowed")
        le.append(nv)

    for i in le:
        o = (i * k) % 53
        t.append(o)
    print(t)
    f2 = open('message.txt', 'w')
    for i in t:
        f2.write(d[i])
    le.clear()
    t.clear()
    f2.close()
def mulinv(r1,r2):
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
        m += 53
    return(m)
def sdecipher():
    li=[]
    k=int(input("enter your key to decrypt:"))
    ki=mulinv(53,k)
    f1 = open('message.txt', 'r')
    inpt = f1.readline()
    f1.close()
    for i in inpt:
        if (ord(i) >= 65 and ord(i) <= 90):
            nv = ord(i) - 65
        elif (ord(i) >= 97 and ord(i) <= 122):
            nv = ord(i) - 71
        elif (ord(i) == 32):
            nv = ord(i) + 20
        else:
            print("unacceptable symbol allowed")
        li.append(nv)
    f1 = open('message.txt', 'w')
    for i in li:
        o = (i * ki) % 53
        f1.write(d[o])
    f1.close()
def tencipher():
	tekey=input("enter key for encipher")
	col=len(tekey)
	with open("message.txt") as f:
		msg=f.read()
	plain=len(msg)

	list(msg)
	x=math.ceil(plain/col)
	row=x
	a=[0]*row
	k=0
	for i in range(row):
		a[i]= [0]*col
	b=[0]*row
	for i in range(row):
		b[i]= [0]*col
	for i in range(row):
		for j in range(col):
			if(k<plain):	
				a[i][j]=msg[k]
				k=k+1
	tekey=list(map(int,tekey))
	for i in range(row):
		for j in range(col):
			new=tekey[j]
			b[i][j]=a[i][new]
	encrypt=list()
	for i in range(row):
		for j in range(col):
			if b[i][j] != 0 :
				encrypt.append(b[i][j])
			else:
				encrypt.append('0')
	encipher=''.join(encrypt)
	print(encipher)
	with open("message.txt","w") as f:
		f.write(encipher)			
def tdecipher():
	tekey=input("enter key for encipher")
	col=len(tekey)
	with open("message.txt") as f:
		msg=f.read()
	plain=len(msg)

	list(msg)
	x=math.ceil(plain/col)
	row=x
	a=[0]*row
	k=0
	for i in range(row):
		a[i]= [0]*col
	b=[0]*row
	for i in range(row):
		b[i]= [0]*col
	for i in range(row):
		for j in range(col):
			if(k<plain):	
				a[i][j]=msg[k]
				k=k+1
	tekey=list(map(int,tekey))
	for i in range(row):
		for j in range(col):
			new=tekey[j]
			b[i][j]=a[i][new]
	decrypt=list()
	for i in range(row):
		for j in range(col):
			if b[i][j] != '0' :
				decrypt.append(b[i][j])
	decipher=''.join(decrypt)
	with open("message.txt","w") as f:
		f.write(decipher)
while True:
    print("press 1 for substitution \n  2 for transposition \n  3 for exit")
    choice=int(input("enter your choice"))
    if choice==1:
        substitution()
    elif choice==2:
        transposition()
    else:
        break
