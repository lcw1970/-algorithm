from collections import deque
import copy
def bfs(x,y) :
    q= deque()
    q.append((x,y))
    while q :
        cx,cy = q.popleft()
        for i in range(4) :
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < h and 0 <= ny < w :
                if graph[nx][ny] == "." :
                    q.append((nx,ny))
                    move[nx][ny] = move[cx][cy] +1
                    graph[nx][ny] = "#"
            elif 0 > nx or nx >= h or 0 >ny or ny >=w :
                return move[cx][cy] +1
    return 0
            
def fire_bfs() :
    q_fire = deque() 
    for i in range(h) :
        for j in range(w) :
           if fire_graph[i][j] == "*" :
               q_fire.append((i,j))
    while q_fire :
        cx,cy = q_fire.popleft()
        for i in range(4) :
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < h and 0 <= ny < w :
                if fire_graph[nx][ny] != "#" :
                    q_fire.append((nx,ny))
                    move_fire[nx][ny] = move_fire[cx][cy] +1
                    fire_graph[nx][ny] = "#"
            elif 0 > nx or nx >= h or 0 >ny or ny >=w :
                return move_fire[cx][cy] +1
    return 1000
                 
t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(t):
    w,h = map(int,input().split())
    graph = []

    move = [[0]*w for _ in range(h)]
    move_fire = [[0]*w for _ in range(h)]

    for _ in range(h) :
        a = list(input())
        graph.append(a)
    fire_graph = copy.deepcopy(graph)
    
    for i in range(h):
        for j in range(w) :
            if graph[i][j] == "@" :
                result =bfs(i,j)
    result_fire = fire_bfs()
    if result > 0 and result < result_fire :
        print(result)
    else :
        print("IMPOSSIBLE")
