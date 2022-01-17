# 코딩테스트 연습 - 해시 - 위장
def solution(clothes):
    answer = 1
    
    clothes.sort(key = lambda x:x[1])
    dic = []
    tmp = 0
    
    for i in clothes :
        if i[1] not in dic :
            answer *= (tmp + 1)
            dic.append(i[1])
            tmp = 1
        elif i[1] in dic :
            tmp += 1
    
    answer = answer * (tmp + 1) - 1
    return answer
