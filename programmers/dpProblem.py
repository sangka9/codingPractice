# 코딩테스트 연습 연습문제 2 x n 타일링
def solution(n):
    answer = 0
    
    l = [0 for i in range(n+1)]
    
    for i in range(1,n+1) :
        if i <= 2 :
            l[i] = i
        else :
            l[i] =  ( l[i-1] + l[i-2] ) % 1000000007
    
    answer = l[n]
    
    return answer
