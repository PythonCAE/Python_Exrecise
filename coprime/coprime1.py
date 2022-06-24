## CASE :1
#To check how many coprime number falls under that number.
# for example between 8:(1,2,3,4,8)
      # 1 ={1} 1 is coprime number of 8
      # 2 = {1,2} isnot coprime number of 8
      # 3 ={1,3} is coprime number of 8
      # 4 ={1,2,4} isnot coprime number of 8
      # 5 ={1,5} is coprime number of 8
      # 6 ={ 1,2,3,6} isnot coprime number of 8
      # 7 = {1,7} is coprime number of 8
# 1,3,5,7 is coprime number of 8 becuase this number dont share the other factorial except than 1

# def coprime1(number):
#     num1 =[]
#     num3 =[1,]
#     for i in range(2,number+1):
#         if number%i ==0:
#             num1.append(i)
#     # print(num1)        
           
#     for j in range(2,number):
#         num2 =[]
#         for k in range(2,j+1):
#            if j%k==0:
#                num2.append(k)
#         print(num2)       
#         for k in num2:
#             if k in num1:
#                 break
#         else:
#            num3.append(j)   

                
#     return num3  

# number = int(input("Enter the number:"))
# a =coprime1(number)
# print(a)


for i in range(2,8):
    a=[]
    if i%2==0:
        a.append(i)
print(a)        



