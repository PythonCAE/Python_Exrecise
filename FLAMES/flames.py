Name1 = input("Enter The  First Name1:")
Name2 =input("Enter The First Name2:")
Total_len =len(Name1)+len(Name2) #For calculating length of Two String
count =0
for i in Name1:#Iterating the First character in for loop
    if i in Name2:# checking  each character of First Name into each second  Name character
        count += 2 #IIF character matched then raised value by 2

Wcount = Total_len -count #Calculating the unmached character from two names
if Wcount>0: #unmatched chracter length is greater than 0
    List1 =["F","L","A","M","E","S"] 
    LenOfList=len(List1) #Calculating the length of List
    Value = Wcount%LenOfList
    ReduceIndex =Value-1 #To cut the matched fcount value in List1 because list strat with zero one number less.
    if len(List1)>=0:#checking length of List which will run until length is greater than one
        Left = List1[:ReduceIndex]#To elemenate or cut that index charcter in List1[0 to index-1]
        Right = List1[ReduceIndex+1:]#To elemenate or cut that index charcter in List1[index+1 to end_index]
        List1 = Right+Left #Combine but in reverse because to start with Chracter next to the cut Character in List
    else:
        List1 = List1[:ReduceIndex-1]
    print(List1[0])      

