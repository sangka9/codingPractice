# 코딩테스트 연습 - 연습문제 - 하샤드 수
def solution(x):
    l = list(str(x))
    sum = 0
    for i in range(len(l)) :
        sum += int(l[i])
    
    if x % sum == 0 :
        return True
    else :
        return False
    #return n % sum([int(c) for c in str(n)]) == 0 한줄 코딩 참고
