'''
     3   5
x + x - x + ...
_   _   _
2!  4!  6!

'''
def fac(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s


n,x=map(int,input('Enter value for n and x').split())
den=2
s,i=0,1
power=1
while n>0:
    s+=(i*((x**power)/fac(den)))
    power+=2
    den+=2
    n-=1
    print(s)
print(s)
    
