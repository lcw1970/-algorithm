from collections import deque

n = int(input())
normal = [list(input()) for _ in range(n)]
m = len(normal[0])
color_blind = list(map(list,normal))
for i in range(n):
    for j in range(m):
        if color_blind[i][j] == "R":  
            color_blind[i][j] = "G"

visit = [[-1] *m for _ in range(n)]
def bfs_normal(x,y,color) :
    q = deque([(x,y)])
    visit[x][y] = 1
    while q :
        x,y = q.popleft()
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)) :
            nx,ny = x + dx,y +dy
            if 0<= nx < n and 0 <= ny < m :
                if normal[nx][ny] == color and visit[nx][ny] == -1 :
                    q.append((nx,ny))
                    visit[nx][ny] = 1

blind_visit = [[-1] *m for _ in range(n)]
def bfs_blind(x,y,color) :
    q = deque([(x,y)])
    blind_visit[x][y] = 1
    while q :
        x,y = q.popleft()
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)) :
            nx,ny = x + dx,y +dy
            if 0<= nx < n and 0 <= ny < m :
                if color_blind[nx][ny] == color and blind_visit[nx][ny] == -1 :
                    q.append((nx,ny))
                    blind_visit[nx][ny] = 1
       
colors = ["R","B","G"]
count_normal = 0
count_blind = 0
for i in range(n) :
    for j in range(m) :
        for c in colors :
            if normal[i][j] == c and visit[i][j] == -1 :
                bfs_normal(i,j,c)
                count_normal += 1

for i in range(n) :
    for j in range(m) :
        for c in colors :
            if color_blind[i][j] == c and blind_visit[i][j] == -1 :
                bfs_blind(i,j,c)
                count_blind += 1
    
            
print(f"{count_normal} {count_blind}")

