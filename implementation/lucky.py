# 내 방식

n = list(map(int,input()))

long = len(n)//2

sum_left = 0
sum_right = 0
for i in n[:long]:
    sum_left += i
for j in n[long:] :
    sum_right += j

if sum_left == sum_right :
    print("LUCKY")

else :
    print("READY")

# 더 깔끔한 코드

n = list(map(int,input()))

half = len(n)//2

if sum(n[:long]) == sum(n[long:]) :
    print("LUCKY")

else :
    print("READY")