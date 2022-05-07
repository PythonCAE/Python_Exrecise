num = int(input("Enter the num:"))
for row in range(num):
    for space in range((num-row-1)):
        print(end=" ")
    for fnum in range(row+1,0,-1):
        print(fnum,end="")
    for bnum in range(2,row+2):
        print(bnum,end="")
    print()        

