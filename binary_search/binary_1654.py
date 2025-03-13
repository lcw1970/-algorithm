n,k = map(int,input().split())

lst = [int(input()) for _ in range(n)]

start = 1
end = max(lst)
result = 0
while (start <= end) :
    mid = (start + end) // 2
    total = 0
    for x in lst :
        total += (x//mid)
    if total >= k :
        result = mid
        start = mid + 1
    else :
        end = mid - 1

print(result)
