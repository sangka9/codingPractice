# 코딩테스트 연습 연습문제 과일 장수
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    for i in range(1,int(len(score)/m)+1) :
        answer += m * score[(i*m)-1]
        
    return answer
