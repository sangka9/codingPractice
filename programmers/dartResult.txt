# 2018 KAKAO BLIND RECRUITMENT - [1차] 다트게임
def solution(dartResult):
    answer = 0
    stack = []
    number = 0
    tmp = 0
    
    for i in range(len(dartResult)) :
        if(dartResult[i] == 'S') :
            stack.append(number)
        elif(dartResult[i] == 'D') :
            stack.append(number**2)
        elif(dartResult[i] == 'T') :
            stack.append(number**3)
        elif(dartResult[i] == '*') :
            stack.append(2)
            answer += tmp
        elif(dartResult[i] == '#') :
            stack.append(-1)
        else :
            if(dartResult[i-1] == '1') and (dartResult[i] == '0') :
                number = 10
            else :
                number = int(dartResult[i])
            if(len(stack) > 0) :
                tmp = 1
                while(len(stack)):
                    tmp *= stack.pop()
                answer += tmp

            
    if(len(stack) > 0) :
        tmp = 1
        while(len(stack)):
            tmp *= stack.pop()
        answer += tmp
    
    return answer
