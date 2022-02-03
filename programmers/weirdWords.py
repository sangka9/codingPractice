# 코딩테스트 연습 - 연습문제 - 이상한 문자 만들기
def solution(s):
    answer = ''
    odd = True
    
    for i in range(len(s)) :
        if s[i] == ' ' :
            answer += ' '
            odd = True
        else :
            if odd == True :
                answer += s[i].upper() 
                odd = False
            else :
                answer += s[i].lower()
                odd = True
    
    return answer
