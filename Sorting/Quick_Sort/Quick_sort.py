

def arrange(L,f,l):
    Pivot = L[f]
    Left = f+1
    Right = l
    while True:
        while Left<=Right and L[Left]<=Pivot:
            Left += 1
        while Left<=Right and L[Right]>=Pivot:
            Right += 1
        if Left > Right:
            break

        else:
            L[Left],L[Right] = L[Right],L[Left]

                
    L[f],L[Right] = L[Right],L[f]

    return Right

def conqure(List,first,last):
    if first>last:
        a = arrange(List,first,last)
        arrange(List,first,a-1)
        arrange(List,a+1,last)

List =[50,40,60,80,20,70]
l = len(List)
conqure(List,0,l-1)    
print(List)
