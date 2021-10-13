# 월간 코드 챌린지 시즌1 - 3진법 뒤집기
def solution(n):
    answer = 0
    ternary = []
    
    while(1) :
        if(n > 0) :
            ternary.append(n%3)
            n = n//3
        else :
            break
    
    ternary.reverse()
    
    for i in range(len(ternary)) :
        answer += ternary[i] * (3**i)
        
    return answer
