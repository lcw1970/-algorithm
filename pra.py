n = int(input())
origin = list(map(int,input().split()))
order = {}

sort_origin = set(origin)
sort_origin = sorted(sort_origin, key=lambda x:x)
for i in range(len(sort_origin)) :
    order[sort_origin[i]] = i

for num in origin :
    print(order[num],end = ' ')