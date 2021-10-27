# 연습문제 - 124 나라의 숫자
def solution(n):
    answer = ''
    
    while 1 :
        tmp = n % 3
        n = n // 3
        if tmp == 0 :
            answer = '4' + answer
            n -= 1
        elif tmp == 1 :
            answer = '1' + answer
        elif tmp == 2 :
            answer = '2' + answer

        if(n == 0) :
            break
    return answer
