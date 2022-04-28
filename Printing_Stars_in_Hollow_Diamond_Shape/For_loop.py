num = int(input("Enter the row and column:"))

for row in range(1,num+1):
    for column in range(1,num+1):
        if row+column==4 or row+column==6 or row+column==8:
            print("*",end="")
        else:
            print(end=" ")    
    print()        