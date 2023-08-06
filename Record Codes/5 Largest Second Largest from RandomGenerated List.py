import random
def generate(l,u):
    randl=[]
    for i in range(l,u+1):
        randl.append(random.randint(l,i))
    return randl

def max_secmax(l):
    large=l[0]
    for i in range(len(l)):
        if l[i] > large:
            large = l[i]
    sec=l[0]
    for i in range(len(l)):
        if l[i] > sec and l[i] != large:
            sec = l[i]
    return large,sec

def prime(l):
    primel=[]
    for i in l:
        f=0
        for fac in range(1,i+1):
            if i % fac == 0:
                f+=1
        if f==2:
            primel.append(i)
    return primel

l=int(input('Enter Lower limit : '))
u=int(input('Enter Upper limit : '))
rlist=generate(l,u)
print('List generated :',rlist)
max1,max2 = max_secmax(rlist)
print('Largest number is',max1,'and the Second largest is',max2,'\nList of prime numbers from the generated list :',prime(rlist))
