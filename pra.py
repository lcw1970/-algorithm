from collections import deque

n = int(input())

q = deque()

for i in range(1,n+1) :
    q.append(i)

while len(q)>1:
    first_card = q.popleft()
    print(first_card,end =" ")
    second_card = q.popleft()
    q.append(second_card)

print(q.popleft())