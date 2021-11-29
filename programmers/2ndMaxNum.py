# 코딩테스트 연습 연습문제 다음 큰 숫자
def solution(n):
    answer = 0
    
    countOne = bin(n).count('1')
    while(1) :
        n = n + 1
        tmpOne = bin(n).count('1')
        if tmpOne == countOne :
            answer = n
            break
    
    return answer
