# 2018 KAKAO BLIND RECRUITMENT - [3차] 압축
def solution(msg):
    answer = []
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    index = 0
    length = 1
    count = 1
    
    while(1) :
        count += 1
        if(msg[index:index+length] in alpha) :
            if(index+length) == len(msg) :
                answer.append(alpha.index(msg[index:index+length]) + 1)
                break
            length += 1
        
        elif(msg[index:index+length] not in alpha) :
            print(f'in {msg[index:index+length-1]}')
            print(f'not in {msg[index:index+length]}')
            alpha.append(msg[index:index+length])
            answer.append(alpha.index(msg[index:index+length-1]) + 1)
            index += length - 1
            length = 1
        
    return answer
