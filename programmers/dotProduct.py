#월간 코드 챌린지 시즌1 - 내적
def solution(a, b):
    answer = 0
    
    for i in range(len(a)) :
        answer += a[i] * b[i]
    
    # return sum([x*y for x,y in zip(a,b)]) zip 활용 방법
    return answer
