num = int(input("Enter the Number:"))
i = 2
string = str(num)
rev = string[::-1]
if string == rev:
    while(num>i):
        if num%i==0 :
            print("Not a  Prime as well but  Palindrom")
            break
        i += 1
    else:
        print("Palindromic Prime Number")  

else:
    while(num>i):
        if num%i==0 :
                print("Not a  Prime as well and not  Palindrom")
                break
        i += 1
    else:
        print("Not a Palindrom but Prime number ")


