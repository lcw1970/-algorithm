from collections import deque
def bfs(x,y,arrive_x,arrive_y) :
    if x == arrive_x and y == arrive_y :
        return 0
    graph[x][y] = 1
    
    q = deque()
    q.append((x,y))
    while q :
        cx,cy = q.popleft()
        for dx,dy in ((-2,-1),(2,-1),(-1,-2),(1,-2),(-2,1),(2,1),(-1,2),(1,2)) :
            nx = cx +dx
            ny = cy +dy
            if 0 <= nx < I and 0 <= ny < I :
                if nx == arrive_x and ny == arrive_y :
                    move[nx][ny] = move[cx][cy] +1
                    return move[nx][ny]
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = 1
                    move[nx][ny] = move[cx][cy] +1
                    q.append((nx,ny))


t = int(input())
for _ in range(t) :
    I = int(input())

    night_x,night_y = map(int,input().split())
    arrive_x,arrive_y = map(int,input().split())

    graph = [[0] * I for _ in range(I)]
    move = [[0] * I for _ in range(I)]

    result = bfs(night_x,night_y,arrive_x,arrive_y)
    print(result)