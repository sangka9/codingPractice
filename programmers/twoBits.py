# 월간 코드 챌린지 시즌2 - 2개 이하로 다른 비트
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)) :
        tmp = numbers[i] + 1
        
        while(1):
            if( bin(numbers[i] ^ tmp).count('1') <= 2 ) :
                answer.append(tmp)
                break
            else :
                tmp += 1
                
    return answer
