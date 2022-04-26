class Using_For_Loop:
    def __init__(self,num):
        self.num=num

    def Show(self):
        for row in range(1,self.num+1):
            Space = row
            for space in range(1,Space):
                print(end=" ")
            Star = self.num-row+1
            for star in range(1,Star+1):
                print("*",end=" ")
        print()  
For=Using_For_Loop(int(input("Enter The No of row:")))
For.Show()               
