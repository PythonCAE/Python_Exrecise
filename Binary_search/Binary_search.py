def find_number(key,List):
    low = 0
    high = len(List)-1
    while high >= low:
        mid = (high+low)//2
        if key == List[mid]:
           print(f'{key} found at {mid} position')
           break
        elif key<List[mid]:
            high = mid-1
        elif key>List[mid]:
            low = mid+1
    else:        
      print(f'{key} not in List')      

List = [1,4,7,10,23,50,100]
key = 50
find_number(key,List)            





                                              




