# num = int(input("Enter the Number:"))
# sum=0

#Using For Loop for the adding its factorial and adding into sum variable:
# for i in range(1,num):
#     if(num%i==0):
#         sum=i+sum
# if sum==num:
#     print("yes")
# else:
#     print("no")    

class Prefect_Number:
    def __init__(self,num):
        self.num=num

    def check_Perfect_Number(self):
        sum=0
        for i in range(1,self.num) :
            if(self.num%i==0):
                sum=i+sum

        if(sum==self.num):
          print("yes")
        else:
         print("no") 

class Show:
    def show(s):
        print(s.check_Perfect_Number())         
num=   int(input("Enter the number:"))     
perfnum= Prefect_Number(num)
Show.show(perfnum)
   

                           
