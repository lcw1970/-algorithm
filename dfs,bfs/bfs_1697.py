from collections import deque

n,k = map(int,input().split())

graph = [-1] * 100001


def bfs(x) :
    if x == k :
        return 0
    graph[x] = 0
    q = deque()
    q.append(x)
    while q: 
        cx = q.popleft()
        move = [-1,1,cx]
        for i in range(3) :
            nx = cx +move[i]
            if 0 <= nx <=100000 :
                if nx == k :
                    graph[nx] =graph[cx] +1
                    return graph[nx]
                if graph[nx] == -1 :
                    graph[nx] =graph[cx] +1
                    q.append(nx)
                
   
a = bfs(n)
print(a)