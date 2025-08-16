n = int(input())
lst= []
for _ in range(n):
    age,name = input().split()
    lst.append((age,name))
sort_lst = sorted(lst,key=lambda x:int(x[0]))

for age,name in sort_lst :
    print(f"{age} {name}")