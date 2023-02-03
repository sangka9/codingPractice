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
