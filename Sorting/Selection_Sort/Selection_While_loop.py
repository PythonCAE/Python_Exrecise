list = []
n = int(input("Enter How Many Number You Want:"))
#For The how many number and what number in list
while(n>0):
    list.append(int(input("Enter the Number:")))
    n -= 1

#First Loop is for the picking First unsorted number in list 
l =len(list) #For the length of list
i = 0
while(l>i):
    Min = list[i] #Set the first unorderd unsorted number is minimum.
    #secon Loop is for the a campare remaing other number to find the minimum.
    j = i
    while(l>j):
        if Min > list[j]: #Checking the First unodered number to remaing unordered number in the list.
            Min = list[j]
        Index = list.index(Min)# It will fin the index of the minimum value in list
        j += 1
    list[i],list[Index] = list[Index],list[i]
    i += 1
print(list)    





