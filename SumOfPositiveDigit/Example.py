Number = int(input("Enter Number:"))
sum = 0
num = Number
l = len(str(Number))
while(num != 0):
    n = num%10
    sum = sum + n
    num =num//10
print(sum)    