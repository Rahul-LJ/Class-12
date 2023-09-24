#THIS IS THE FIRST PART OF 9th code
def palindrome(n):
    NUM,num = n,0
    while n > 0:
        rem = n % 10
        num = num*10 + rem
        n //= 10
    if NUM == num:
        return 1
    else:
        return -1

def special(n):
    NUM,s = n,0
    while n>0:
        num = n%10
        n//=10
        ss = 1
        for i in range(1,num+1):
            ss*=i
        s+=ss
    if NUM == s:
        return 1
    else:
        return -1
