size = int(input("Enter the number of size of rows and column:"))

#For the number of the rows:
for row in range(1,size+1):
    #for the number of the column:
    for column in range(1,row+1):
        print("*",end="")
    print()    

