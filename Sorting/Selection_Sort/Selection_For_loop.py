list = []
n = int(input("Enter the how number you need:"))
for i in range(n):
    list.append(int(input("Enter Number:")))

l =len(list)
for i in range((l)):
    Min = list[i]
    for j in range(i+1,l):
        if Min>list[j]:
            Min = list[j]
        Index = list.index(Min)
    list[i],list[Index] = list[Index],list[i]
print(list)               
    
    
  

    
