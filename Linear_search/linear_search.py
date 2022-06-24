def linear_search(cards,query):
    # create a variable position with 0
    position = 0
    # set loop for iteration
    while True:
        #check if element at the current position match the query
        if cards[position] == query:
            #Answer found!!! returnning the position
            return position
        position += 1
        #check if position reached at end of the array
        if position == len(cards):
            return -1

test = {
    'input':{
             'cards':[13,11,10,7,4,3,1,0],
             'query':7
            },
    'output': 3       
}
print(test)
result = linear_search(test['input']['cards'],test['input']['query'])
print(result)
output = test['output'] 
print(output)
print(result == output)              
