def binary(array,target,start,end) :
    while start<= end :
        mid = (start + end)//2
        if array[mid] == target :
            return 1
        elif array[mid] > target :
            end = mid - 1
        else :
            start = mid +1
    return 0


n = int(input())
n_lst = list(map(int,input().split()))
n_lst.sort()

# -10, 2, 3, 6, 10 
#   0, 1, 2, 3, 4 
m = int(input())
m_lst = list(map(int,input().split()))

for target in m_lst :
    result = binary(n_lst,target,0,n-1)
    print(result,end=" ")