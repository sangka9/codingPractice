# 코딩테스트 연습 - 연습문제 - JadenCase 문자열 만들기
def solution(s):
    answer = ''
    up = 1

    for i in range(len(s)) :   
        if up == 1 :
            answer += s[i].upper()
        else :
            answer += s[i].lower()
        up = 0
        
        if s[i] == " " :
            up = 1
    
    return answer
