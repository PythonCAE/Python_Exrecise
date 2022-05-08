List = [10,15,4,23,0]
l = len(List)
for i in range(l):
    for j in range(l-1):
        if List[j]>List[j+1]:
            List[j],List[j+1] = List[j+1],List[j]

print(List)            