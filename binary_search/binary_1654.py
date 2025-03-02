import sys
input = sys.stdin.readline
k,n = map(int, input().split())
len_cables = [int(input().strip()) for _ in range(k)]

start, end = 1,max(len_cables)
result = 0
while start<= end :
    mid = (start+end) // 2
    count = 0
    for lan in len_cables :
        count += lan // mid
    
    if count >=n :
        result = mid
        start = mid + 1
    else :
        end = mid - 1

print(result)
