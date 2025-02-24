from collections import deque

n, m = map(int,input().split())
graph = []
visit = [[False] * m for _ in range(n)]

for _ in range(n) :
    data = list(map(int,input()))
    graph.append(data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
    visit[x][y] = True
    q = deque()
    q.append((x,y))
    while q :
        cx,cy = q.popleft()
        for i in range(4):
            nx,ny = cx + dx[i],cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and graph[nx][ny] == 1:
                visit[nx][ny] = True  # 방문 처리
                graph[nx][ny] = graph[cx][cy] +1
                q.append((nx, ny))  # 큐에 좌표 추가
        
bfs(0,0)
print(graph[n-1][m-1]) 