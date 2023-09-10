#Code By PiyushVarman

import MATRIX as mat
l=[]
n=int(input("Enter the number of rows and columns in the square matrix:"))
for i in range(n):
    print("\nRow number",i+1)
    temp=[]
    for j in range(n):
        temp.append(int(input("Enter the number for column "+str(j+1)+":")))
    l.append(temp)
mat.SWAP(l)
mat.SORTROWCOL(l)
