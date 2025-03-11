n,c = map(int,input().split())

lst = list(map(int,input().split()))
dic = {}
order = {}
count = 1
for i in lst :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1
        order[i] = count
        count += 1

lst_sort = sorted(lst, key=lambda x:(-dic[x],order[x]))

print(lst_sort)