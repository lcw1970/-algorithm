n,c = map(int,input().split())

lst = list(map(int,input().split()))
dic = {}
order = {}

for i,num in enumerate(lst) :
    if num in dic :
        dic[num] += 1
    else :
        dic[num] = 1
        order[num] = i
        

lst_sort = sorted(lst, key=lambda x:(-dic[x],order[x]))

print(*lst_sort)