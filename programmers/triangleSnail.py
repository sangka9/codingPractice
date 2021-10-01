# 월간 코드 챌린지 시즌1 - 삼각 달팽이
def solution(n):
    answer = []
    box = [[] for i in range(n+1)]
    down = 0
    right = 1
    up = 0
    index = 0
    num = 1
    
    for i in range(1,n+1) :
        for j in range(1,n+2-i) :
            if(i % 3 == 1) : # down
                index += 1
                box[index].insert(down,num)
                num += 1
            elif(i % 3 == 2) : # right
                box[index].insert(right,num)
                right += 1
                num += 1
            elif(i % 3 == 0) : # up
                index -= 1
                box[index].insert(len(box[index])+up,num)
                num += 1
            
        if(i % 3 == 1) : down += 1
        elif(i % 3 == 2) : right = down + 1
        elif(i % 3 == 0) : up -= 1
    
    for i in range(len(box)) :
        for j in range(len(box[i])) :
            answer.append(box[i][j])
            
    return answer
