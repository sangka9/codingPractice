
#코딩테스트 연습 - 연습문제 - 정수 제곱근 판별
def solution(n):
    answer = 0
    
    sqrt = n**(1/2)
    
    if sqrt % 1 == 0 :
        answer = (sqrt+1)**2
    else :
        answer -= 1
        
    return answer
