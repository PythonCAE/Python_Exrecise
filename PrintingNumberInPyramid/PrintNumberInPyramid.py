row = int(input("Enter the num:"))

count = 0
while(row>count):
    space = row-count-1
    while(space>0):
        print(end=" ")
        space -= 1
    number = count + 1
    while(number>0):
        print(number,end="")
        number -= 1
    number = count
    bnumber =2  
    while(number > 0):
        print(bnumber,end="")
        bnumber += 1
        number -= 1 

    count += 1    
    print( )


