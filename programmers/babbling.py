# 코딩테스트 연습 연습문제 옹알이 (2)
def solution(babbling):
    answer = 0
    b = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)) :
        index = 0
        skip = 5
        while 1 :
            tmp = index
            for j in range(4) :
                if babbling[i].startswith(b[j],index,index+len(b[j])) and j != skip :
                    index += len(b[j])
                    skip = j
                    break
            if tmp == index :
                break
            elif tmp != index :
                if index == len(babbling[i]) :
                    answer += 1
                    break
    
    return answer
