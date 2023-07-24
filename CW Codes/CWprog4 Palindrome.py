'''WAP to input a string and check if its a palindrome implementing
A) without function
B) UDF with argument
C) UDF with argument returning boolean value'''

s=input('Enter string: ')
s=s.lower()

#A
if s==s[::-1]:
    print('Its a palindrome')
else:
    print('Its not a palindrome')


#B
def pal(s):
    if s==s[::-1]:
        print('Its a palindrome')
    else:
        print('Its not a palindrome')

pal(s)


#C
def palbol(s):
    return(s==s[::-1])
print(palbol(s))                    #returns True or False
