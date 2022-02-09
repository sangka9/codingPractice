# 코딩테스트 연습 - 연습문제 - 시저 암호
def solution(s, n):
    answer = ''
    l = list(s)
    
    for i in range(len(l)) :
        if l[i] != ' ' :
            if l[i].isupper() and ord(l[i])+n > 90:
                answer += chr(ord(l[i])+n-26)
            elif l[i].islower() and ord(l[i])+n > 122:
                answer += chr(ord(l[i])+n-26)
            else :
                answer += chr(ord(l[i])+n)
        else :
            answer += ' '
    return answer
