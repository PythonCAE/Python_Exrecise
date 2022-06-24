Year = int(input("Enter  a Year:"))

if Year%4==0:
    if Year%100==0:
        if Year%400==0:
            print("Leap Year")
        else:
            print(" Not Leap Year")    
    else:
        print("leap year")    
else:
    print("Not A Leap Year")    

