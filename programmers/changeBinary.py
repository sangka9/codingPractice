#월간 코드 챌린지 시즌1 - 이진 변환 반복하기
def solution(s):
    answer = [0, 0]
    
    while(s != "1") :
        one = s.count("1")
        zero = s.count("0")
        
        answer[0] += 1
        answer[1] += zero
        
        s = bin(one)
        s = s[2:]
        
    return answer
