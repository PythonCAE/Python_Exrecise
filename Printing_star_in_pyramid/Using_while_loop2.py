size =  int(input("Enter the number of Rows:"))

#let set value of number of rows:
row = 1

#Using While Loop for setting number of Row:
while(row<size+1):
    space=size-row # For The number of space before star
    while(space>0): #It will print space.
        print(end=" ")
        space =space- 1
    star = row 
    while(star>0): #For printing star
        print("*",end=" ")
        star =star - 1    
    row += 1
    print()    

