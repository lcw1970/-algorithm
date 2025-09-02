graph = []

move = [0,1,2,3] # 북 동 남 서 +3을 하고 %4 하면 왼쪽방향

dx = [-1,0,1,0] 
dy = [0,1,0,-1]
n,m = map(int,input().split())
x,y,c = map(int,input().split())
visit = [[False]*m for _ in range(n)]

for _ in range(n) :
    line = list(map(int,input().split()))
    graph.append(line)
count = 1
turn_time = 0
visit[x][y] = True
while True :
    c = (c + 3) %4
    nx = x +dx[c]
    ny = y +dx[c]
    if 0 <= nx <n and 0 <= ny <m :
        if graph[nx][ny] == 0 and visit[nx][ny] == False:
            count += 1
            turn_time = 0
            visit[nx][ny] = True
            x,y= nx,ny
            continue
            
    turn_time += 1 
    if turn_time == 4 :
        d = (c+2) % 4
        nx = x +dx[d]
        ny = y +dy[d]
        if graph[nx][ny] == 1:
            break
        elif graph[nx][ny] == 0 :
            x,y = nx,ny
            turn_time = 0

print(count)
