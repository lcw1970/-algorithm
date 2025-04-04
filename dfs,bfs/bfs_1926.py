from collections import deque
n,m = map(int,input().split())
graph = []
big = 0
for _ in range(n) :
    graph.append(list(map(int,input().split())))

def bfs(x,y) :
    global big
    size = 1
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    while q :
        cx,cy = q.popleft()
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)) :
            nx = cx+dx
            ny = cy+dy
            if 0 <= nx < n and 0<=ny<m :
                if graph[nx][ny]== 1 :
                    q.append((nx,ny))
                    graph[nx][ny] = 0
                    size += 1
    if size > big :
        big = size
                    


count = 0
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            bfs(i,j)
            count += 1

print(count)
print(big)