# Summer / Winter Coding(~2018) - 예산
def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for i in range(len(d)) :
        if(budget-d[i] >= 0) :
            budget = budget - d[i]
            answer += 1
        else :
            break
    
    return answer
