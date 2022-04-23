i=int(input("Enter the Number of rows:"))
j=int(input("Enter the Number of rows:"))

for rows in range(1,i+1):  # for Number of Rows
    for columns in range(1,j+1): #for the Numbe of Columns
        if rows == i or rows+columns==5 or columns-rows==3:
            print("*",end="")
        else:
            print(end=" ")    
    print()        


