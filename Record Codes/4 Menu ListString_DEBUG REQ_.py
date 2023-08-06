def binsearch(x,l):
    low,high = 0,len(l)-1
    while low <= high:
        middle = (low+high) // 2
        if l[middle] == x:
            return middle
        elif l[middle] < x:
            low = middle+1
        else:
            high = middle-1
    return -1    #if middle is NOT returned

def rev(s):
    return s[::-1]

while True:
    m=int(input('1 Binary Search in a list of strings \n2 Reverse a string \n3 Exit \nChoose your option: '))
    if m==1:
        n=int(input('Enter number of elements in the list: '))
        l=[]
        for i in range(1,n+1):
            l.append(int(input('Enter element '+str(i))))
        x=int(input('Enter the number to be searched: '))
        if binsearch(x,l) != -1:
            print(x,' is found in the list at ',binsearch(x,l))
        else:
            print(x,' is not found in the list.')
        print()

    elif m==2:
        s=input('Enter string: ')
        print('Reversed string is ',rev(s))
        print()

    elif m==3:
        break
