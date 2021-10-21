# 2019 KAKAO BLIND RECRUITMENT - 오픈채팅방
def solution(record):
    answer = []
    dic = {}
    sp =[]
    
    for i in range(len(record)):
        sp = record[i].split()
        
        if(sp[0] == 'Enter') or (sp[0] == 'Change'):
                dic[sp[1]] = sp[2]
    
    for i in range(len(record)) :
        sp = record[i].split()
        
        if(sp[0] == 'Enter') :
            answer.append(f'{dic[sp[1]]}님이 들어왔습니다.')
        elif(sp[0] == 'Leave') :
            answer.append(f'{dic[sp[1]]}님이 나갔습니다.')
    
    return answer
