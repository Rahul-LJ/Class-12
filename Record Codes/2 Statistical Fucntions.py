def mean(l):
    s=0
    for i in l:
        s+=i
    return s

def median(l):
    l.sort()
    if len(l)%2 == 0:
        return (l[len(l)/2]+l[len(l)/2+1])/2
    else:
        return l[len(l)//2+1]

def mode(l):
    count={}
    for integers in set(l):
        c=0
        for i in l:
            if integers == i:
                c+=1
        count[integers]=c
    return max(count, key=count.get)

n=int(input('Enter number of elements in the list: '))
l=[]
for i in range(n):
    l.append(int(input('Element '+str(i+1))))
print('Mean: ',mean(l),'\nMedian: ',median(l),'\nMode: ',mode(l))
