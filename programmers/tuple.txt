# 2019 카카오 개발자 겨울 인턴십 - 튜플
import re
def solution(s):
    answer = []
    t = s.split('}')
    n = [[] for i in range(len(t)-2)]
    
    for i in range(len(t)) :
        numbers = re.findall(r'\d+', t[i])
        if(len(numbers) > 0) :
            n[len(numbers)-1] = list(map(int, numbers))
        
    answer.append(n[0][0])
    for i in range(1,len(n)) :
        tmp = list(set(n[i]) - set(n[i-1]))
        answer.insert(len(answer),tmp[0])
    
    return answer
