n,x = map(int,input().split())
lst = list(map(int,input().split()))

dic = {}

for i in lst :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1

if x in dic :
    print(dic[x])
else :
    print(-1)