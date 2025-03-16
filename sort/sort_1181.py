n = int(input())
lst = []
for _ in range(n) :
    lst.append(input())

lst = set(lst)

sort_lst = sorted(lst,key=lambda x:(len(x),x))

for i in sort_lst :
    print(i)