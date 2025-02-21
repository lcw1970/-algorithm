# dfs 기초 덩어리 찾는 문제


# 문제:
# 2D 격자에서 연결된 1의 개수를 셀 때, 하나의 1이 다른 1과 상하좌우로 연결되어 있는 경우를 하나의 덩어리로 본다. 즉, 1들이 연결된 영역의 개수를 구하는 문제.

# 입력:
# 첫 번째 줄에 N, M (격자의 세로, 가로 크기)이 주어진다. (1 ≤ N, M ≤ 100)
# 그 다음 N개의 줄에 M개의 값으로 격자의 상태가 주어진다. (1은 땅, 0은 물)
# 출력:

# 연결된 1들의 덩어리 개수를 출력하라.
# 예시 입력:
# 4 5
# 1 1 0 0 0
# 1 1 0 1 0
# 0 0 0 1 1
# 0 0 1 1 1

# 예시 출력:
# 2
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