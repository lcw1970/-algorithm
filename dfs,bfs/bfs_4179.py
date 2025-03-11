from collections import deque 

n,m = map(int,input().split())
grid = []
dist = [[-1]*m for _ in range(n)]
fire_dist = [[-1]*m for _ in range(n)]

for _ in range(n) :
    grid.append(list(input()))
q = deque()
fire_q = deque()
for i in range(n) :
    for j in range(m) :
        if grid[i][j] == "J" :
            q.append((i,j))
            dist[i][j] = 0
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                print(1)
                exit()
        if grid[i][j] == "F":
            fire_q.append((i,j))
            fire_dist[i][j] = 0

while fire_q :
    x,y = fire_q.popleft()
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)) :
        nx,ny = dx+x,dy+y 
        if 0<= nx < n and 0 <= ny < m :
            if grid[nx][ny] == "." and fire_dist[nx][ny] == -1 :
                fire_dist[nx][ny] = fire_dist[x][y] +1
                fire_q.append((nx,ny))

while q :
    x,y = q.popleft()
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)) :
        nx,ny = dx+x,dy+y 
        if 0<= nx < n and 0 <= ny < m :
            if grid[nx][ny] == "." and dist[nx][ny] == -1 :
                if fire_dist[nx][ny] == -1 or dist[x][y]+1 < fire_dist[nx][ny] :
                    dist[nx][ny] = dist[x][y] +1
                    q.append((nx,ny))
        else :
            print(dist[x][y] +1)
            exit()

print("IMPOSSIBLE")