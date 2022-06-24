# def tri_recursion(k):
#     if(k>0):
#         result = k+tri_recursion(k-1)
#         print(result)
#     else:
#       result = 0
#     return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

def ff(n):
    if n ==1:
        return 0
    else:
        result = n* ff(n-1)
        print(result)    
ff(6)        