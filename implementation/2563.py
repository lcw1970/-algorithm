t = int(input())

lst = [[0]*101 for _ in range(101)]

for _ in range(t):
    x,y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            lst[i][j] = 1
count = 0
for i in range(100):
    for j in range(100):
        if lst[i][j]== 1:
            count +=1
print(count)