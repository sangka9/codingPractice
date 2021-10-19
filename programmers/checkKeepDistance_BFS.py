# 2021 카카오 채용연계형 인턴십 - 거리두기 확인하기
from collections import deque

def solution(places):
    answer = []
    
    for i in range(len(places)) :
        
        for x in range(len(places[i])) :
            correct = 1
            for y in range(len(places[i][x])) :
                start = [x,y,0]
                if(places[i][x][y] == 'P') :
                    result = findDistance(places[i],start)
                    if result == False :
                        correct = 0 
                        break
            if correct == 0 :
                break
        answer.append(correct)
    return answer

def findDistance(box, s) :
    
    visited = [[0]*len(box) for i in range(len(box[0]))]
    de = deque([s])
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    
    while de :
        x,y,c = de.popleft()
        visited[x][y] = 1
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            nc = c + 1
            
            if 0 <= nx < len(box) and 0 <= ny < len(box[0]) and not visited[nx][ny] :
                visited[nx][ny] = True
                
                if box[nx][ny] == 'P' :
                    if nc <= 2 :
                        return False
                elif box[nx][ny] == 'O' :
                    if nc == 1:
                        de.append([nx,ny,nc])
                        
    return True
        
