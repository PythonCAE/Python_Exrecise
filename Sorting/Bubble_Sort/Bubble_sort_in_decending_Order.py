#Part 1
List = []
n =  int(input("Enter how many Number:"))
for i in range(n):
    List.append(int(input("Enter the Number")))
for i in range(n,0,-1):
    for j in range(n-1,0,-1):
        if List[j] > List[j-1]:
            List[j-1],List[j] = List[j],List[j-1]

print(List)


#Part 2
List = []
n =  int(input("Enter how many Number:"))
while(n>0):
    List.append(int(input("Enter the Number:")))
    n -= 1
l = len(List)
i = 0
while(l>i):
    j = l-1
    k =0
    while(j>k):
        if List[j] > List[j-1]:
            List[j-1],List[j] = List[j],List[j-1]        
        j -= 1
    i += 1
print(List)               