# 찾아라 프로그래밍 마에스터 - 게임 맵 최단거리 # BFS 경로 찾기
def solution(maps):
    answer = BFS_Maps(maps)
    return answer

def BFS_Maps(maps) :
    #방문경로
    visited = [[0]*len(maps[0]) for i in range(len(maps))]
    #좌/우/위/아래 방향
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    
    #BFS 경로 탐색, queue 방식
    queue = [(0,0)]
    visited[0][0] = 1
    
    while queue :
        x, y = queue.pop(0) # 시작점
        
        if x == len(maps)-1 and y == len(maps[0])-1 :
            print(visited[x][y])
            break
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) :
                if visited[nx][ny] == 0 and maps[nx][ny] == 1 :
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny)) # 경로 저장
    
    if(visited[len(visited)-1][len(visited[0])-1]) :
        return visited[len(visited)-1][len(visited[0])-1]
    else :
        return -1
