# 코딩테스트 연습 연습문제 멀리 뛰기
def solution(n):
    answer = 0
    l = [0 for i in range(n+1)]
    
    for i in range(1,n+1) :
        if i <= 2 :
            l[i] = i
        elif i > 2 :
            l[i] = l[i-1] + l[i-2]
    

    answer = l[n] % 1234567
    
    return answer
