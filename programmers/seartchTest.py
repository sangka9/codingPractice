# 코딩테스트 연습 - 완전탐색 - 모의고사
def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    correct = []
    
    correct.append(numOfCorrect(answers,num1))
    correct.append(numOfCorrect(answers,num2))
    correct.append(numOfCorrect(answers,num3))
    
    m = max(correct)
    answer = [i+1 for i,v in enumerate(correct) if v == m]
    
    return answer
    
def numOfCorrect(answers, n) :
    correct = 0
    for i in range(len(answers)) :
        if(answers[i%len(answers)] == n[i%len(n)]) :
            correct += 1
    
    return correct
