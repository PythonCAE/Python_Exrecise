# num = int(input("Enter the number of Rows:")) 
# for row in range(1,num+1):
#     space = num-row
#     for sp in range(1,space+1):
#         print(end=" ")
#     star = row
#     for sta in range(star):
#         print("*",end=" ")
#     print()        

n= int(input("Enter the number of rows:"))
for i in range(0,n):
    print(" "*i,end="")
    print("* "*(n-i))