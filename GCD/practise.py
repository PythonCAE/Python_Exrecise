def GCD(a,b):
    if b ==0:
        return a
    else:
        return GCD(b,a%b)
a = int(input("Enter First Number:"))
b = int(input("Enter the Second Number:"))
c = GCD(a,b)
print(c)            