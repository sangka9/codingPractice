# 코딩테스트 연습 연습문제 콜라 문제
def solution(a, b, n):
    answer = 0
    
    while n >= a :
        tmp = n
        answer += int(tmp/a)*b
        n = int(n/a)*b + int(n%a)
    
    return answer
