#write a python program to accept a list, then update the list by adding 1 to all even numbers and minus 1 to all odd numbers
l=[]
n=int(input('Enter the no of elements: '))
for i in range(1,n+1):
    l.append(int(input('Element '+str(i)+': ')))
print('The list : ',l)

for num in range(n):
    if l[num] % 2 == 0:
        l[num]+=1
    else:
        l[num]-=1
print(l)
