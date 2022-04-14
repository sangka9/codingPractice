# 코딩테스트 연습 - 연습문제 - 숫자의 표현
def solution(n):
    answer = 0
    tmp = 0
    arr = [0 for i in range(n+1)]
    half = int(n/2)
    arr[n] += 1
    
    for i in range(1,half + 1) :
        for j in range(i,half + 2) :
            tmp += j
            if tmp < n+1 :
                arr[tmp] += 1
            else :
                break
        tmp = 0
        
    answer = arr[n]
    
    return answer
