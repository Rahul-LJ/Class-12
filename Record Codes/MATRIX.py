#Code By PiyushVarman

'''USER DEFINED MODULE 2
AIM: To create an user defined module MATRIX to include 2 user defined functions SWAP(),
SORTROWCOL() and import this module in another python code and execute the functions
METHODOLOGY: A module MATRIX is created to include the 2 functions namely SWAP()
which takes a nested list of integers as parameter and swaps the main and secondary
diagonal elements; SORTROWCOL() which takes a nested list of integers as parameter and
sorts each row in ascending order using Bubble sort followed by each column in ascending
order using Insertion sort.
This module is imported in another python code and both the functions are executed with
the outputs displayed in the main function.
Note: Create a module MATRIX to include the functions, with each function to include
docstrings to describe the function. Also write a python code to import this module and use the
two functions for inputs from the user.
i) swap() to take as parameter a nested list and swaps the left and right diagonal elements. This
function to be tested with a nested list of integers
ii) sortrowcol() – takes as parameter a nested list of integers and sorts the rows using bubble
sort in ascending order and sorts columns using Insertion sort in ascending order. This function
to be tested with a nested list of integers.
Both the outputs to be shown in the main function'''

def matprint(l):
    print()
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],end=' ')
        print()
    print()
def SWAP(l):
    print("\nThe Matrix you have entered is:")
    matprint(l)
    for i in range(len(l)):
        x1,y1,x2,y2=0,0,0,0
        temp1,temp2=0,0
        for j in range(len(l[i])):
            if i==j:
                temp1=l[i][j]
                x1,y1=i,j
            if i+j==2:
                temp2=l[i][j]
                x2,y2=i,j
        l[x2][y2]=temp1
        l[x1][y1]=temp2
    print("The modified Matrix is:")
    matprint(l)
def SORTROWCOL(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            for z in range(j,len(l[i])):
                if l[i][j]>l[i][z]:
                    l[i][j],l[i][z]=l[i][z],l[i][j]
    print("The Matrix sorted by rows is:")
    matprint(l)
    
    for i in range(len(l)):
        for j in range(len(l[i])):
            for z in range(j,len(l[i])):
                if l[j][i]>l[z][i]:
                    l[j][i],l[z][i]=l[z][i],l[j][i]
    print("The Matrix sorted by columns is:")
    matprint(l)
    
