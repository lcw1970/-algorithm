a = input().split('-')
for i in range(len(a)) :
    a[i] = sum(map(int,a[i].split("+")))

result = a[0]
for i in range(1,len(a)):
    result -= a[i]

print(result)