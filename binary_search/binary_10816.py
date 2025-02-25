import sys
input = sys.stdin.readline

n = int(input().strip())
n_lst = list(map(int,input().split()))
m = int(input().strip())
m_lst = list(map(int, input().split()))
n_lst.sort()

n_dic = {}
for num in n_lst :
    if num in n_dic :
        n_dic[num] += 1
    else :
        n_dic[num] = 1

def binary(array,target,start,end) :
    while start <= end :
        mid = (start+end) //2
        if array[mid] == target :
            return n_dic.get(target,0)
        elif array[mid] > target :
            end = mid-1
        else :
            start = mid +1
    
    return 0

for target in m_lst :
    print(binary(n_lst,target,0,n-1),end = ' ')

