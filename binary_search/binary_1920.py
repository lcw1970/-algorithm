def binary(array,target,start,end) :
    while start <= end :
        mid = (start + end) //2 
        if array[mid] == target :
            return 1
        elif array[mid] > target :
            end = mid-1
        else :
            start = mid +1
        
    return 0

n = int(input())
n_lst= list(map(int,input().split()))
m = int(input())
m_lst = list(map(int,input().split()))

n_lst.sort()
for i in m_lst :
    print(binary(n_lst,i,0,n-1))