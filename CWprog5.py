'''WAP implementing function to input 2 string and check if both the strings with 5 vowals
A) with return
B) without return'''

s1=input('Enter string 1:')
s2=input('Enter string 2:')
v=['a','e','i','o','u']

def vcheck(s1,s2):
    c1,c2=0,0
    for x in s1:
        if x in v:
            c1+=1
    for y in s2:
        if y in v:
            c2+=1
    if c1==c2:
        if c1==5:
            print('Yes')       #without return
        else:
            print('No')
    else:
        print('No')

vcheck(s1,s2)

def vcheck_return(s1,s2):
    c1,c2=0,0
    for x in s1:
        if x in v:
            c1+=1
    for y in s2:
        if y in v:
            c2+=1
    if c1==c2:
        return c1==5            #return

print(vcheck_return(s1,s2))

