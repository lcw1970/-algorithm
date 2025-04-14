n = int(input())
array = list(map(int,input().split()))
m = int(input())

start = 1
end = max(array)
def binary(start,end,array,target) :
    result= 0
    while (start <= end) :
        mid = (start+end) // 2
        total = 0
        for money in array :
            if money > mid :
                money = mid
            total += money
        if total <= target :
            result = mid 
            start = mid + 1
        else :
            end = mid - 1
    return result
result = binary(start,end,array,m)
print(result)