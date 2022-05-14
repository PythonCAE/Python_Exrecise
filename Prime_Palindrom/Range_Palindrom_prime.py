num1 = int(input("Enter the Number1:"))
num2 = int(input("Enter the Number2:"))
while(num2>num1):
    i = 2
    string = str(num1)
    rev = string[::-1]
    if string == rev:
        while(num1>i):
            if num1%i==0  :
                # print("Not a  Prime as well not Palindrom")
                break
            i += 1

            
        else:
            print(num1)    
     
    num1 += 1       
    
