'''UDF to print Tuple of Prime numbers between 2 numbers'''

def prime(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f+=1
    if f==2:
        return True
    else:
        return False


def primetuple(l,u):
    t=()
    for i in range(l,u+1):
        if prime(i)==True:
            temp=(i,)
            t=t+temp
    print(t)

primetuple(6,30)
