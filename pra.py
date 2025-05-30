from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
graph = []

for _ in range(n):
    lst = list(map(int,input().split()))
    graph.append(lst)

def bfs(x,y) :
    visited = [[0]*m for _ in range(n)]
    graph_move = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    if graph[x][y] == 2 :
        return 0
    else :
        q = deque()
        q.append((x,y))
        while q :
            nx,ny = q.popleft()
            for i in range(4) :
                cx = nx + dx[i]
                cy = ny + dy[i]
                if 0<= cx < n and 0 <= cy < m and visited[cx][cy] == 0:
                    if graph[cx][cy] == 2 :
                        return graph_move[nx][ny] +1
                    elif graph[cx][cy] == 1 :
                        graph_move[cx][cy] = graph_move[nx][ny] +1
                        q.append((cx,cy))
                        visited[nx][ny]= 1
        return -1  
for i in range(n):
    for j in range(m):
        result = bfs(i,j)
        print(result,end = " ")       
    print()