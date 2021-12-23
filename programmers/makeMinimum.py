# 코딩테스트 연습 - 연습문제 - 최솟값 만들기
def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    B.reverse()

    for i,j in zip(A,B) :
        answer += i*j
    
    return answer
