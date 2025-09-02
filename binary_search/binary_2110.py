def binary(start,end,target,array) :
    result = 0
    while start <= end :
        mid = (start + end)//2 
        count = install(mid,array)
        if count >= target :
            result = mid 
            start = mid + 1
        else :
            end = mid - 1
    return result

def install(mid,array):
    count = 1
    last = array[0]
    for i in range(1,n) :
        if (array[i] -last) >= mid :
            count += 1
            last = array[i]
    return count

n,c = map(int,input().split())
house = []

for _ in range(n) :
    h = int(input())
    house.append(h)
house.sort()

start = 1
end = house[-1] - house[0]

result = binary(start,end,c,house)
print(result)