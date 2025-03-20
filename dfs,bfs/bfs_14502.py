from collections import deque
import copy
from itertools import combinations
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus(array) :
    q = deque()
    for i in range(n) :
        for j in range(m) :
            if array[i][j] == 2 :
                q.append((i,j))
    while q :
        cx,cy = q.popleft()
        for i in range(4) :
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0 <= nx<n and 0 <=ny < m and array[nx][ny]== 0  :
                q.append((nx,ny))
                array[nx][ny] = 2
def count_safe(array):
    count = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0 :
                count += 1
    return count

n,m = map(int,input().split())
graph = []
result = 0

for _ in range(n) :
    line = list(map(int,input().split()))
    graph.append(line)

empty = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))


for comb in combinations(empty, 3):
    temp_graph = copy.deepcopy(graph)
    for x, y in comb:
        temp_graph[x][y] = 1
    virus(temp_graph)
    safe = count_safe(temp_graph)
    if safe > result:
        result = safe
print(result)

