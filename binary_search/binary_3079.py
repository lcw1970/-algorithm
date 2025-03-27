def binary(array,target,start,end) :
    result = 0
    while start <= end :
        mid = (start+end)//2
        total = 0 
        for time in array :
            total +=(mid //time)
        if total >= target :
            result = mid
            end = mid -1
        else :
            start = mid +1
    return result

n,m = map(int,input().split())
time_lst = []
for _ in range(n) :
    a = int(input())
    time_lst.append(a)

time_lst.sort()
start = 1
end = max(time_lst) *m

result = binary(time_lst,m,start,end)
print(result)