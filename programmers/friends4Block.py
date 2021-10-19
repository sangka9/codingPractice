# 2018 KAKAO BLIND RECRUITMENT - [1차] 프렌즈4블록
import re

def solution(m, n, board):
    answer = 0
    
    for i in range(len(board)) :
        board[i] = list(board[i])
    
    while (1) :
        index = []
        
        for i in range(m-1) : # 4박스 찾기
            for j in range(n-1) :
                if is4Block(board,i,j) :
                    index.append([i,j])
        
        if(len(index) == 0) : # 종료조건
            break
        
        while (1) : # 4박스 제거
            if(len(index) > 0) :
                answer += deleteBlock(board,index.pop(0))
            else :
                break       

        cleanBlock(board) # 4박스 제거 후 정렬
        
    return answer

def is4Block(box,x,y) :
    if(box[x][y] == box[x+1][y]) and (box[x+1][y] == box[x+1][y+1]) and (box[x][y] == box[x][y+1]) and (box[x][y]).isalpha() :
        return True
    else :
        return False

def deleteBlock(box,i) :
    x = i[0]
    y = i[1]
    cnt = 0
    if(box[x][y] != '8') :
        box[x][y] = '8'
        cnt += 1
    if(box[x+1][y] != '8') :
        box[x+1][y] = '8'
        cnt += 1
    if(box[x][y+1] != '8') :
        box[x][y+1] = '8'
        cnt += 1
    if(box[x+1][y+1] != '8') :
        box[x+1][y+1] = '8'
        cnt += 1
    return cnt

def cleanBlock(box) :
    
    changeBox = [[]*len(box) for _ in range(len(box[0]))]
    
    for y in range(len(box[0])) :
        tmp = []
        for x in range(len(box)) :
            tmp.append(box[x][y])
        tmp = ''.join(tmp)
        tmp = re.findall(r'[A-Z]+', tmp)
        tmp = ''.join(tmp)
        while(len(tmp) <= x) : # 틀렸던 부분 조심!
            tmp = '8' + tmp

        for x in range(len(box)-1,-1,-1) :
            changeBox[x].append(tmp[x]) # 여기까지 틀렸던부분!

    for i in range(len(box)) :
        box[i] = changeBox[i]
