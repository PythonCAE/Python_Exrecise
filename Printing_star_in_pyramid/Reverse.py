num = int(input("Enter the row:"))
row=1
while(row<num+1):
    space = row-1
    while(space>0):
        print(end=" ")
        space -= 1
    star = num-row+1
    while(star>0):
        print("*",end=" ")
        star -= 1
    row += 1
    print()        