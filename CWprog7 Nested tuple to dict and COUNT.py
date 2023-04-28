'''WAP which accepts a tupe of strings and
counts the number of occurances of each string and
stores the string and its count as key value pair in a dictionary'''

def count(l,i):        #UDF instead of using built in .count()
    c=0
    for k in l:
        if k==i:
            c+=1
    return c

def count_tup(t):
    dic={}              #converting data tup to list
    l=[]
    for i in t:
        for j in i:
            l.append(j) 

    for elements in set(l):                #set has elements without repetition
        dic[elements]=count(l,elements)     #counts that element in the new list
    return dic

t=eval(input('Enter tuple: '))
print(count_tup(t))

'''Credits to @JEs-TAR for sloving this'''
