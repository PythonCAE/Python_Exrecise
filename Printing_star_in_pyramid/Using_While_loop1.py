row = int(input("Enter the number for row:"))
column =int(input("Enter the number of column:"))
i=1
while(i<row+1):
    j=1
    while(j<column+1):
        if i+j==5 or (i+j==7 and i!=1) or (i+j==9 and i!=2) or (i==row and j%2 != 0):
            print("*",end="")
        else:
            print(end=" ")
        j=j+1
    i += 1
    print()            