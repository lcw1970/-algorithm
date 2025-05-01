from collections import deque

n,m = map(int,input().split())
graph = []


for _ in range(n) :
    graph.append(list(input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
    visit = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((x,y))
    visit[x][y] = 0
    while q :
        cx,cy = q.popleft()
        for i in range(4) :
            nx = cx +dx[i]
            ny = cy +dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if visit[nx][ny] == -1 and graph[nx][ny]== "L":
                    visit[nx][ny] = visit[cx][cy] +1
                    q.append((nx,ny))
    return max(map(max,visit))


big = 0
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == "L" :
            result = bfs(i,j) 
            if result > big :
                big = result
print(big)