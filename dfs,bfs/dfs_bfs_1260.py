import sys 
from collections import deque

input = sys.stdin.readline
n,m,v = map(int,input().split())

visit_dfs = [False] * (n+1)
visit_bfs = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    one,two = map(int,input().split())
    graph[one].append(two)
    graph[two].append(one)
def dfs(x) :
    print(x, end = ' ')
    visit_dfs[x] = True
    for i in graph[x] :
        if not visit_dfs[i] :
            dfs(i)

def bfs(x) :
    visit_bfs[x] = True
    q =deque()
    q.append(x)
    while q :
        num = q.popleft()
        print(num,end = ' ')
        for i in graph[num] :
            if not visit_bfs[i] :
                visit_bfs[i] = True
                q.append(i)

dfs(v)
print()
bfs(v)