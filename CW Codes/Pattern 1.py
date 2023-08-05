'''
UDF to print following pattern using N.

A#1
C*A*3
E#C#A#5
G*E*C*A*7

'''

def pattern(n):
    num=1
    for rows in range(n):
        if rows%2==0:
            symbol='#'
        else:
            symbol='*'
        for letters in range(64+num,64,-2):
            print(chr(letters),end=symbol)
        print(num)
        num+=2

n=int(input())
pattern(n)
