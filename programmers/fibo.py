# 코딩테스트 연습 - 연습문제 - 피보나치 수
def solution(n):
    answer = 0
    
    fibo = [0 for i in range(100001)]
    
    for i in range(100001) :
        if i == 0 :
            fibo[i] = 0
        elif i == 1 :
            fibo[i] = 1
        else :
            fibo[i] = fibo[i-1] + fibo[i-2]
    
    answer = fibo[n] % 1234567
    
    return answer
