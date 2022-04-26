def Star_Triangle(size):
    #For the Row:
    row=1
    while(row<size+1):
        #For the Column:
        column=1
        while(column<row+1):
            print("*",end="")
            column += 1
        print() 
        row += 1

Star_Triangle(int(input("Enter the size:")))           