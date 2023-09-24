def fac(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def fib(n):
    a,b=-1,1
    for i in range(n):
        print(a+b,end=',')
        a,b=b,a+b

while True:
    m=int(input("1) Factorial of a number \n2) Generate 'N' Fibonacci series \n3) Exit \nChoose your option: "))
    if m==1:
        n=int(input('Enter number to find its factorial: '))
        print(n,'! is ',fac(n))
        print()

    elif m==2:
        n=int(input('Enter number to find its fibonacci series: '))
        fib(n)
        print()

    elif m==3:
        break
