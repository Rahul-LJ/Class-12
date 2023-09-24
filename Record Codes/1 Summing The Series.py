def fac(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

while True:
    m = int(input('''Compute the sum of the following series:
i) x^1 - x^3 + x^5 - x^7 + ... 'n' terms
   ___   ___   ___   ___
    2!    4!    6!    8!

ii) x^1 - x^3 + x^5 - x^7 + ... 'n' terms
   ___   ___   ___   ___
    3!    5!    7!    9!

Choose your option 1 or 2 (3 to quit): '''))
    if m == 1:
        t,sign = 0,1
        power = 1
        den = 2
        n = int(input('Enter number of terms : '))
        x = int(input('Enter value of x : '))
        for i in range(n):
            t += (x^power)/fac(den)
            power += 2
            den += 2
            sign *= -1
        print('The sum is',t)

    if m == 2:
        t,sign = 0,1
        power = 1
        den = 3
        n = int(input('Enter number of terms : '))
        x = int(input('Enter value of x : '))
        for i in range(n):
            t += (x^power)/fac(den)
            power += 2
            den += 2
            sign *= -1
        print('The sum is',t)

    if m == 3:
        print('Code ended successfully ;)')
        break
