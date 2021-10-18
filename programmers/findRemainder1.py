#월간 코드 챌린지 시즌3 - 나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    x = 1
    while (1) :
        if(n % x == 1) :
            answer = x
            break
        else :
            x += 1
    return answer
