#월간 코드 챌린지 시즌2 괄호 회전하기
def solution(s):
    answer = 0

    for i in range(len(s)) :
        if(isCorrect(s)) :
            answer += 1

        s = s[1:] + s[0]

    return answer

def isCorrect(x) :
    stack = []
    stack.append(x[0])
    t = x[1:]
    
    if(len(x)%2 == 1) :
        return False
    
    while(1) :        
        if stack[-1] == '(' and t[0] == ')' :
            stack.pop()
            t = t[1:]
        elif stack[-1] == '[' and t[0] == ']' :
            stack.pop()
            t = t[1:]
        elif stack[-1] == '{' and t[0] == '}' :
            stack.pop()
            t = t[1:]
        else :
            stack.append(t[0])    
            t = t[1:]
        
        if len(stack) == 0 :
            if(len(t) == 1) :
                stack.append(t[0])
                break
            elif(len(t) > 1) :
                stack.append(t[0])
                t = t[1:]
            else :
                break
        
        if(len(t) == 0):
            break

    if(len(stack) == 0) :
        return True
    else :
        return False
