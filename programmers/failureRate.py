# 2019 KAKAO BLIND RECRUITMENT - 실패율
def solution(N, stages):
    answer = []
    counting = []
    failure = []
    tmp = 0
    
    counting.append(0)
    for i in range(1, N + 1) :
        counting.append(stages.count(i))
        if(len(stages) - tmp) != 0 :
            failure.append(counting[i] / (len(stages) - tmp))
        else :
            failure.append(0)
        tmp += counting[i]
        
    n = len(failure)
    
    while(n) :
        m = failure.index(max(failure))
        answer.append(m+1)
        failure[m] = -1
        n = n - 1
    
    return answer
