# 코딩테스트 연습 연습문제 푸드 파이트 대회
def solution(food):
    answer = ''
    
    for i in range(1,len(food)) :
        tmp = int(food[i]/2)
        answer += str(str(i) * tmp)
    
    return answer + '0' + answer[::-1]
