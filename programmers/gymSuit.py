# 코딩테스트 연습 - 탐욕법(Greedy) - 체육복
def solution(n, lost, reserve):
    answer = 0
    
    clothes = [1 for i in range(n)]
    
    for i in range(len(clothes)) :
        if i+1 in lost :
            clothes[i] -= 1
        if i+1 in reserve :
            clothes[i] += 1
            
    for i in range(len(clothes)) :
        if clothes[i] > 0 :
            answer += 1
            clothes[i] -= 1
        elif clothes[i] == 0 :
            if i > 0 and clothes[i-1] == 1 :
                    answer += 1
                    clothes[i-1] -= 1
            elif i+1 < len(clothes) and clothes[i+1] == 2 :
                    answer += 1
                    clothes[i+1] -= 1
    
    return answer
