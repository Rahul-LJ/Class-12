'''WAP to def DIV_list() where number list is a list of numbers passes as arguments.
fucntion returns 2 lists, d2 and d5 which stores num divisible by 2 and 5 respetively'''


def DIV_list(*n):              #  *n adds n arguments
    l=[*n]
    d2,d5=[],[]
    for i in l:
        if i%2==0:
            d2.append(i)
        if i%5==0:
            d5.append(i)
        else:
            continue
    print('List D2: ',d2)
    print('List D2: ',d5)

DIV_list(1,2,3,4,5,6,7,8,9,10)  #sample inputs
