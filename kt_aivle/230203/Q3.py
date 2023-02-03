# Q3 answer template

def solution(store, customer):
    answer = []
    
    for i in range(len(customer)) :
        if customer[i] in store :
            answer.append('yes')
        else :
            answer.append('no')
    
    return answer

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)

##########################################

# Q3 answer template

def solution(store, customer):
    answer = []
    clist = [0 for i in range(101)]
    slist = [0 for i in range(101)]
    
    for i in range(len(store)) : slist[store[i]] = 1
        
    for i in range(len(customer)) : clist[customer[i]] = 1
    
    for i in range(len(customer)) :
        if clist[customer[i]] and slist[customer[i]] :
            answer.append('yes')
        else :
            answer.append('no')
    
    return answer

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)
