# 백준 2606 - 바이러스 
# dfs
n = int(input())
m = int(input())
count = 0
graph = [[] for _ in range(n+1)]
visit = [False] *(n+1)
for _ in range(m) :
    one,two = map(int,input().split())
    graph[one].append(two)
    graph[two].append(one)

def dfs(x) :
    global count 
    visit[x] = True 
    for i in graph[x] :
        if visit[i] == False :
            count += 1
            dfs(i)

dfs(1)
print(count)

# bfs
from collections import deque

n = int(input()) # 컴퓨터의 수 
m = int(input()) # 컴퓨터에 연결된 쌍의 수
visit = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    one,two = map(int,input().split())
    graph[one].append(two)
    graph[two].append(one)
def bfs(x) :
    visit[x] = True
    count = 0
    queue = deque()
    queue.append(x)
    while queue :
        num = queue.popleft()
        for i in graph[num] :
            if visit[i] == False :
                visit[i] = True
                count += 1
                queue.append(i)
    return count

print(bfs(1))