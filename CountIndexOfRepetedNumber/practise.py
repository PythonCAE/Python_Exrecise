def CountIndex(list,number):
    count = []
    for i in range(len(list)):
        if number == list[i]:
            count.append(i)
    return count        

list =[1,3,4,8,7,11,1,15]
number =int(input("Enter the Number:"))
c =CountIndex(list,number)    
print(c)
