#코딩테스트 연습 연습문제 숫자 짝꿍
def solution(X, Y):
    answer = ''
    
    xNum = list(X)
    yNum = list(Y)
    
    for i in range(9,-1,-1) :
        xx = 0
        yy = 0
        if str(i) in xNum :
            xx = xNum.count(str(i))
        if str(i) in yNum :
            yy = yNum.count(str(i))
            
        answer += str(i) * min(xx,yy)
    
    if len(answer) == 0 :
        return "-1"
    elif answer[0] == '0' :
        return "0"
    
    return answer
