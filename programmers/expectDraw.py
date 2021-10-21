# 2017 팁스타운 - 예상 대진표
def solution(n,a,b):
    answer = 0
    
    while(1) :
        answer += 1
        if (a - b == 1) and (b + 1) // 2 != (b // 2) :
            break
        elif (b - a == 1) and (a + 1) // 2 != (a // 2) :
            break
        else :
            if(a % 2 == 0) :
                a = a / 2
            else :
                a = (a + 1) / 2
            if(b % 2 == 0) :
                b = b / 2
            else :
                b = (b + 1) / 2
    
    return answer
