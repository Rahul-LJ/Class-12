#THIS IS THE FIRST PART OF 9th code
'''USER DEFINED MODULE – 1
AIM: To create an user defined module NUMBER to include 2 user defined functions
PALINDROME(), SPECIAL() and import this module in another python code and execute the
functions
METHODOLOGY: A module NUMBER is created to include the 2 functions namely
PALINDROME() which takes a number as parameter and returns 1 if it’s a palindrome and -1
otherwise; SPECIAL() which takes a number as parameter and returns 1 if it’s a special
number and -1 otherwise.
This module is imported in another python code and both the functions are executed. For the
PALINDROME() function, a tuple of integers are read and the code displays all the palindrome
numbers in the tuple. If there weren’t any palindrome numbers appropriate message is
shown. For the SPECIAL() function 2 limits are read and all the special numbers between
these limits are generated. If there were no special numbers, appropriate message is shown.
Note: Create a module NUMBER to include the functions, with each function to include
docstrings to describe the function. Also write a python code to import this module and use the
two functions for inputs from the user.
i) palindrome() to take as parameter a number and returns 1 if the number is a palindrome and
–1 otherwise. This function to be tested with a tuple of integers
ii) special() – takes as parameter a number and returns 1 if it’s a special number and -1
otherwise. [ A special number is a number equal to the sum of the factorial of the individual
digits of the number] This function to be tested to generate list of special numbers between
two limits accepted from the user.
'''

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
