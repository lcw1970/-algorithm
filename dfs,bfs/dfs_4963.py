import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
while (True) :
    m,n= map(int, input().split())

    count = 0
    if n == 0 and m == 0 :
        break

    graph = []
    visit = [[0]*m for _ in range(n)]

    for _ in range(n) :
        map_data = list(map(int,input().split()))
        graph.append(map_data)

    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]

    def dfs(x,y) :
        visit[x][y] = True
        for i in range(8) :
            nx = dx[i] +x
            ny = dy[i] +y
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and graph[nx][ny] == 1 :
                dfs(nx,ny) 
                    
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 and not visit[i][j]  :
                dfs(i,j)
                count += 1
    print(count)