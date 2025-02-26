n = int(input())
lst = []
for _ in range(n) :
    age,name = input().split()
    lst.append((int(age),name))

sort_lst = sorted(lst,key =lambda x:x[0])

for age,name in sort_lst :
    print(age,name)