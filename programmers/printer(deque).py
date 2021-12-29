# 코딩테스트 연습 - 스택/큐 - 프린터
from collections import deque
def solution(priorities, location):
    answer = 0
    deq = deque()
    for i in range(len(priorities)) :
        deq.append((priorities[i],i))
    
    while 1 :
        if deq[0][0] == max(deq)[0] :
            answer += 1
            if deq.popleft()[1] == location :
                break
        else :
            tmp = deq[0]
            deq.popleft()
            deq.append(tmp)
        
    return answer
