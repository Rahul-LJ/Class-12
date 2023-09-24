import MATRIX as m
l=[]
print("OUTPUT")
n=int(input("Enter the number of rows and columns in the square matrix:"))
for i in range(n):
    print("\nRow number",i+1)
    temp=[]
    for j in range(n):
        temp.append(int(input("Enter the number for column "+str(j+1)+":")))
    l.append(temp)
m.SWAP(l)
m.SORTROWCOL(l)
