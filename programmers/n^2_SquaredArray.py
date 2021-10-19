# 월간 코드 챌린지 시즌3 - n^2 배열 자르기
def solution(n, left, right):
    answer = []
    index = 0
    
    for i in range(n) :
        
        #left 건너뛰기
        if(index < left - n) :
            index += n
            continue
        
        tmp = [k for k in range(i,0,-1)]
        for j in range(n) :
            if(j < i) and left <= index < right+1:
                answer.append(j+1+tmp[j])
            elif left <= index < right+1 :
                answer.append(j+1)
            elif index >= right + 1 : # right 건너뛰기
                break
            index += 1
        if index >= right + 1 :  # right index 초과시 종료
            break
    
    return answer
