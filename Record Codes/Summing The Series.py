'''
x - x3 + x5 - x7 + ...
--  --   --   --
2!  4!   6!   8!
'''
def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def power(n,p):
    return n**p

while True:
    m=int(input('''x - x3 + x5 - x7 + ...
--  --   --   --
2!  4!   6!   8!


x - x3 + x5 - x7 + ...
--  --   --   --
3!  5!   7!   9!

Exit
Choose your option : '''))
    if m==1:
        x=int(input('Enter value of x: '))
        n=int(input('Enter value of n: '))
        s,p=0,1
        for i in range(n):
            s+= (power(x,p))/factorial(p+1)
        print('The sum of first type of series is ',s)
        continue

    if m==2:
        x=int(input('Enter value of x: '))
        n=int(input('Enter value of n: '))
        s,p=0,1
        for i in range(n):
            s+= (power(x,p))/factorial(p+2)
        print('The sum of second type of series is ',s)
        continue

    if m==3:
        break
