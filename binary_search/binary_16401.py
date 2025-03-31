m,n = map(int,input().split())
snacks = list(map(int,input().split()))

def binary(start,end,target,array) :
    result= 0
    while start <= end :
        mid = (start+end) // 2
        total = 0
        for snack in array :
            if snack >= mid :
                total += snack//mid
        if total >= target :
            result = mid
            start = mid + 1
        else :
            end = mid -1
    return result

start = 1
end = max(snacks)

result= binary(start,end,m,snacks)
print(result)