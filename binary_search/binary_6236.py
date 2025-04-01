def binary(start,end,target,array) :
    result = 0
    while start <= end :
        mid = (start + end)// 2
        count = fun(mid,array)
        if count <= target :
            result = mid
            end = mid - 1
        else :
            start = mid + 1
    return result

def fun(mid,array) :
    count = 1
    a = mid 
    for money in array :
        if a < money :
            count += 1
            a = mid
        a -= money
    return count

n,m=map(int,input().split())
money = []
for _ in range(n):
    coin = int(input())
    money.append(coin)

start = max(money)
end = sum(money)
target = m

result = binary(start,end,target,money)
print(result)