FirstNumber = int(input("Enter the first Number:"))
SecondNumber = int(input("Enter the second Number:"))
if FirstNumber>SecondNumber:
    HighNumber = FirstNumber
    LowNumber = SecondNumber
else:
    HighNumber = SecondNumber
    LowNumber = FirstNumber

while(LowNumber != 0):
    remainder = HighNumber%LowNumber
    times  = int(HighNumber/LowNumber)   
    HighNumber = times*LowNumber + remainder
    HighNumber = LowNumber
    LowNumber = remainder
print(HighNumber)         

