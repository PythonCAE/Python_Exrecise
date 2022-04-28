num = int(input("Enter the number row and column:"))
row=1
while(row<num+1):
   column=1
   while(column<num+1):
      if row+column ==4 or column-row==2 or column+row==8 or row-column==2:
         print("*",end="")
      else:
         print(end=" ")
      column += 1
   row += 1      
   print()         
