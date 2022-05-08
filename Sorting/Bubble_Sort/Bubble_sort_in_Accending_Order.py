#Part 1
List = [10,15,4,23,0]
l = len(List)
for i in range(l):
    for j in range(l-1):
        if List[j]>List[j+1]:
            List[j],List[j+1] = List[j+1],List[j]

print(List)   

#Part2
List =[23,15,10,4,0]
l = len(List)
i = 0
while(l>i):
    j = 0
    while(l-1>j):
        if List[j]>List[j+1]:
            List[j],List[j+1] = List[j+1],List[j]
        j += 1
    i += 1
print(List)               