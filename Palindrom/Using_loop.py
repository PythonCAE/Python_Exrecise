# For Interger
Number = int(input("Enter The Number:"))
Num = Number
num = str(Number)
l = len(num)
n = 0
while(Num != 0):
    a = Num%10
    n =n*10 + a
    Num = Num//10
print(n) 

#For String
String = input("Enter the Word:")
l = len(String)
rev_String = ""
for  i in String:
    rev_String = i +rev_String
if String == rev_String:
    print("Palindrom String")
else:
    print("Not Palindrom String")     

