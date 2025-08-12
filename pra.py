n = int(input())

lst = list(map(int,input().split()))

big = max(lst)
result = 0
for i in lst :
    result += i/big*100

print(result/len(lst))