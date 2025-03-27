# [S1] 2343 - 기타 레슨
# 18 1,
def binary(array,start,end,target) :
    result = 0
    while start <= end:
        mid = (start+end)//2 
        total = 0
        count = 1
        for i in array :
            if total+i <= mid :
                total += i
              
            else : 
                total = i
                count += 1
        if count <= target :
            result = mid 
            end = mid -1
        else :
            start = mid +1
    return result
n,m = map(int,input().split())

lst = list(map(int,input().split()))

start = max(lst)
end = sum(lst)

result = binary(lst,start,end,m)
print(result)

