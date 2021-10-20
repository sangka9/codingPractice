# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) - 행렬 테두리 회전하기
def solution(rows, columns, queries):
    answer = []
    board = [[]*columns for _ in range(rows)]
    num = 1
    
    for i in range(rows) :
        for j in range(columns) :
            board[i].append(num)
            num += 1
    
    for i in range(len(queries)) :
        answer.append(rotateBorder(queries[i],board))
    
    return answer

def rotateBorder(q,b) :
    x1,y1,x2,y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
    tmp = b[x1][y1]
    small = b[x1][y1]
    
    for y in range(y1+1,y2+1,1) :
        tmp2 = b[x1][y]
        b[x1][y] = tmp
        tmp = tmp2
        if(tmp < small) :
            small = tmp   
    
    for x in range(x1+1,x2+1,1) :
        tmp2 = b[x][y2]
        b[x][y2] = tmp
        tmp = tmp2
        if(tmp < small) :
            small = tmp
            
    for y in range(y2-1,y1-1,-1) :
        tmp2 = b[x2][y]
        b[x2][y] = tmp
        tmp = tmp2
        if(tmp < small) :
            small = tmp
            
    for x in range(x2-1,x1-1,-1) :
        tmp2 = b[x][y1]
        b[x][y1] = tmp
        tmp = tmp2
        if(tmp < small) :
            small = tmp
            
    return small
