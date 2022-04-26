size=int(input("Enter the number of rows and column:"))
row=1
while(row<size+1):
    column=1
    while(column<row+1):
        print("*",end="")
        column +=1
    row += 1
    print( )        