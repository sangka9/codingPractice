# 코딩테스트 연습 연습문제 삼총사
import itertools
def solution(number):
    answer = 0
    
    l = list(itertools.combinations(number,3))
    
    for i in range(len(l)) :
        if sum(l[i]) == 0 :
            answer += 1
    
    return answer
