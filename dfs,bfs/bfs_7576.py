from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph) :
    q = deque()
    lastday= 0
    for i in range(n) :
        for j in range(m):
            if graph[i][j] == 1 :
                q.append((i,j))
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if graph[nx][ny] == 0 :
                    q.append((nx,ny))
                    graph[nx][ny] =1 
                    move[nx][ny] = move[x][y] + 1
                    lastday = max(lastday,move[nx][ny])
    return lastday
m,n = map(int,input().split())
graph = []
move = [[0]*m for _ in range(n)]
for _ in range(n):
    line = list(map(int,input().split()))
    graph.append(line)

lastday = bfs(graph)
for o in range(n):
    for k in range(m) :
        if graph[o][k] == 0 :
            lastday = -1

print(lastday)