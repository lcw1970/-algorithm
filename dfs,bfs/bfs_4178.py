from collections import deque 

n,m = map(int,input().split())
grid = []
dist = [[-1]*m for _ in range(n)]
for _ in range(n) :
    grid.append(list(input()))

def bfs(x,y) :
    q = deque([(x,y)])
    grid[x][y] = "#"
    dist[x][y] = 1
    while q :
        x,y = q.popleft()
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)) :
            nx,ny = x +dx, y +dy
            if 0<= nx < n and 0<= ny<m and grid[nx][ny]== "." :
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] +1
                grid[nx][ny] = "#"
                
                if nx == 0 or nx == n-1 or ny == 0 or ny == m-1 :
                    return dist[nx][ny]
    return "IMPOSSIBLE"

found = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == "J":
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print(1)
            else :
                print(bfs(i,j))
            exit()
