import sys 
input = sys.stdin.readline
n = int(input().strip())
lst =[]

for _ in range(n) :
    lst.append(int(input().strip()))
if n == 0 :
    print(0)
else :
    lst.sort()
    delx = int(n*0.15+0.5)

    n_lst = lst[delx:n-delx]
    print(int(sum(n_lst)/len(n_lst)+0.5))

