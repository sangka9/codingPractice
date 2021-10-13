# 월간 코드 챌린지 시즌2 - 2개 이하로 다른 비트
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)) :
        if(numbers[i] % 4 != 3) :
            answer.append(numbers[i] + 1)
        else :
            tmp = bin(numbers[i])
            tmp = "0" + tmp[2:]
            
            for i in range(len(tmp)-1,-1,-1) :
                if(tmp[i] == "0") :
                    tmp = tmp [0:i] + "10" + tmp[i+2:]
                    break
            answer.append(int(tmp,2))
            
    return answer
