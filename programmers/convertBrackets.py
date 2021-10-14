# 2020 KAKAO BLIND RECRUITMENT 괄호 변환
def solution(p):
    answer = ''  
    answer = balanceBrackets(p)
    
    return answer

def balanceBrackets(p) :
    if len(p) == 0 :
        return ''
    
    u, v = '', ''
    index = 2
    
    while(1) : # u와 v로 분리
        left = p[:index].count('(')
        right = p[:index].count(')')
            
        if left == right :
            u = p[:index]
            v = p[index:]
            break
        index += 2
    
    #u가 올바른 괄호 문자열인지 확인
    stack = []
    t = u[1:]
    stack.append(u[0])
    
    while(1) :
        if stack[-1] == '(' and t[0] == ')' : 
            stack.pop()
            t = t[1:]
        else :
            stack.append(t[0])
            t = t[1:]
        
        if len(t) == 0 :
            break
    
    if(len(stack) == 0) : # u가 올바른 괄호 문자열 인 경우
        return u + balanceBrackets(v)
    else : # u가 올바른 괄호 문자열 아닌 경우
        t = '(' + balanceBrackets(v) + ')'
        u = u[1:len(u)-1]
        for i in range(len(u)) :
            if u[i] == '(' :
                t += ')'
            else :
                t += '('
        print(t)
        return t
