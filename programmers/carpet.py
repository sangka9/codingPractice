# 코딩테스트 연습 - 완전탐색 - 카펫
def solution(brown, yellow):
    answer = []

    for a in range(3,2501) :
        for b in range(1,a+1) :
            if 2*(a+b)-4 == brown and (a*b) == brown+yellow :
                answer.append(a)
                answer.append(b)
                break
    
    return answer
