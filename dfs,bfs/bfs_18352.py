from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
count = [0] *(n+1)
for _ in range(m) :
    one,two = map(int,input().split())
    graph[one].append(two)
    


def bfs(a) :
    visit[a] = True
    q = deque()
    q.append(a)
    while q :
        num= q.popleft()
        for i in graph[num] :
            if not visit[i] :
                visit[i] = True
                q.append(i)
                count[i] =count[num]+1
bfs(x)
true= False
for i in range(1,n+1) :
    if count[i] == k :
            print(i)
            true = True
    
if not true :
     print(-1)