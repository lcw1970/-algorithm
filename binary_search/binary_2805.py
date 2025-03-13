n,m = map(int,input().split())
lst = list(map(int,input().split()))

h = 0
start = 1
end = max(lst) 

while (start<=end) :
    total = 0
    mid = (start + end) // 2
    
    for x in lst :
        if x >mid :
            total += (x-mid)

    if total >= m :
        h = mid
        start = mid + 1
    else :
        end = mid -1

print(h)