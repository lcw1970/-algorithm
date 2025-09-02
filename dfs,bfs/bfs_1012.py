from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,graph,m,n) :
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    while q :
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx <n and 0 <= ny < m :
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = 0 
                    q.append((nx,ny))



t = int(input())


for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    count = 0
    for _ in range(k):
        b,a = map(int,input().split())
        graph[a][b] = 1

    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 :
                bfs(i,j,graph,m,n) 
                count += 1
    print(count)
