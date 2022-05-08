List = []
n =  int(input("Enter how many Number:"))
for i in range(n):
    List.append(int(input("Enter the Number")))
for i in range(n,0,-1):
    for j in range(n-1,0,-1):
        if List[j] > List[j-1]:
            List[j-1],List[j] = List[j],List[j-1]

print(List)
# a =()
# print(a[0])