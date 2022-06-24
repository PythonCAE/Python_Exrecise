def coprime(bignumber,smallnumber):
    bignum =[]
    smallnum =[]
    for num in range(3,bignumber+1):
        if bignumber%num ==0:
            bignum.append(num)

    for num in range(3,smallnumber+1):
        if smallnumber%num ==0:
            smallnum.append(num)    
    for i in bignum:
        if i in smallnum:
            print(f'{smallnumber} is not coprime number of {bignumber}') 
            break
    else:
        print(f'{smallnumber} is  coprime number of {bignumber}')    

bignumber = int(input("Enter the big number:"))     
smallnumber = int(input("Enter the second number:"))          

coprime(bignumber,smallnumber)    



