import NUMBER

t=()
c=0
for i in range(1,int(input('Enter Number of numbers:'))+1):
    t+=(int(input('Enter number'+str(i))),)
paltuple = ()
for i in t:
    if NUMBER.palindrome(i) == 1:
        paltuple += (i,)
        c = 1 # flag, just to check
if c == 1:
    print('Tuple of palidrome elements is/are:')
    for i in paltuple:
        print(i)
else:
    print('None of the elements are palindrome.')
c=0
l = int(input('Enter lower limit:'))
u = int(input('Enter upper limit:'))
splL = []
for i in range(l,u+1):
    if NUMBER.special(i) == 1:
        splL.append(i)
        c = 1
if c == 1:
    print('Special number beteen',l,'and',u,'is/are:')
    for j in splL:
        print(j)
else:
    print('No special number between',l,'and',u)
