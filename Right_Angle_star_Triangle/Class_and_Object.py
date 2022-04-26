class Star_rectangle:
    def __init__(self,size):
        self.size = size
    def show(self):
        #For the row:
        row = 1
        while(row<self.size+1):
            #For the Column:
            column = 1
            while(column<row+1):
                print("*",end="")
                column += 1
            row += 1
            print() 
star = Star_rectangle(int(input("Enter the size:")))
star.show()                   