#WAP implementing 1 positional argument n to find and return factorial of given number.

def fac(n):
    facsum=1
    for i in range(1,n+1):
        facsum*=i
    return(facsum)

n=int(input('Enter number: '))
print(fac(n))

