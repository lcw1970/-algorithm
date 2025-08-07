from collections import deque

q = deque([1,3])

num = list(input())

result = 0
weight = 0

for i in num:
    if i == "*":
        weight = q[0]
    else :
        result += q[0]*int(i)

    q.rotate(-1)

for i in range(10) :
    if (result+i*weight) % 10 == 0 :
        print(i)
        break
