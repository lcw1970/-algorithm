n, m = map(int,input().split())
graph = []
visit = [[False]*m for _ in range(n)]
count = 0
for _ in range(n) :
    data = list(map(int,input().split()))
    graph.append(data)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y) :
    if graph[x][y] == 0 :
        return False
    visit[x][y] = True
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if not visit[nx][ny] and graph[nx][ny] == 1 :
                dfs(nx,ny)
    return True
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 and not visit[i][j]:  # 방문한 적 없고 1인 경우에만 dfs 실행
            if dfs(i,j) :
                count += 1
print(count)