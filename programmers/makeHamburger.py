# 코딩테스트 연습 연습문제 햄버거 만들기
def solution(ingredient):
    answer = 0
    hamburger = ''

    for i in range(len(ingredient)) :
        if ingredient[i] == 1 :
            if len(hamburger) >= 3 :
                if hamburger[-3:] == '123' :
                    hamburger = hamburger[:-3]
                    answer += 1
                else :
                    hamburger += str(ingredient[i])
            else :
                hamburger += str(ingredient[i])
        else :
            hamburger += str(ingredient[i])
    
    return answer
