from collections import deque

n = int(input())
m = int(input())

queue = deque()
lst = list(map(int,input().split()))

dic = {}


delete = lst[0]
for student in lst :
    if student in dic :
        dic[student] += 1
        continue
    
    
    if len(queue) < n :
        queue.append(student) 
        dic[student] = 1   
    else :
        delete = min(queue,key=lambda x:dic[x])
        queue.remove(delete)
        del dic[delete]

        queue.append(student)
        dic[student] = 1
print(*sorted(queue))