from collections import deque
import copy

def bfs(x,y,array) :
    q = deque()
    q.append((x,y))
    while q :
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx +dx[i]
            ny = cy +dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if array[nx][ny] != 0 :
                    q.append((nx,ny))
                    array[nx][ny] = 0
                    
def max_high(array) :
    result = 0
    for i in range(n) :
        for j in range(n) :
           if array[i][j] > result :
               result = array[i][j]
    return result
 
def count(array) :
    result = 0
    for i in range(n) :
        for j in range(n) :
            if array[i][j] != 0 :
                bfs(i,j,array)
                result += 1
    return result

def get_max_count(high,array) :
    max_count = 0
    for rain in range(0,high+1) :
        rain_graph = copy.deepcopy(array)
        for i in range(n) :
            for j in range(n):
                if rain_graph[i][j] <= rain :
                    rain_graph[i][j] = 0

        result = count(rain_graph)
        if result > max_count :
            max_count = result
    return max_count

n = int(input())
graph = []
for _ in range(n) :
    a = list(map(int,input().split()))
    graph.append(a)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

high = max_high(graph)
max_count = get_max_count(high,graph)
print(max_count)