num = int(input("Enter the Number of the rows and column:"))
n_list=[[0 for row in range(num)] for column in range(num) ]
  
n=1


loop= int((num+1)/2)
start_loop = 0
high = num -1 
low =0

# for i in range(loop):
#     for j in range(low,num):
#         n_list[i][j] = n
#         n = n+1
#     for j in range(high-1,low-1,-1):
#             n_list[high][j]=n
#             n=n+1

while(loop>start_loop):
    low = 0
    while(num>low):
        n_list[start_loop][low] = n
        n = n+1
        low = low+1
    low =1    
    while(num>low):
        n_list[low][high] = n
        n = n+1
        low = low+1  
        
    low = 1  
    hig = high-1 
    while(num>low):
        n_list[high][hig] = n
        n = n+1
        low = low+1
        hig = hig -1

    low = 3
    hig = high-1
    while((num)>low):
        n_list[hig][loop] = n
        n= n+1
        low = low+1
        hig = hig -1



    start_loop = start_loop + 1

    # high = high-1
    # low = low +1

   


    






# while(start_loop>loop):
#     high = num-1
#     low = 0
#     while(high>low):
#         n_list[start_loop][low]=n
#         n = n + 1
#         low += 1
        

          




        

row=0
while(row<num):
    column=0
    while(column<num):
        print(n_list[row][column],end="\t")
        column += 1
    row += 1
    print()     
