# 1 2 3 4 5 6
# 1 3 6 10 15 21
# 1 4 10 20 35 
# 1 5 15 35 70
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    zero = [i for i in range(1,n+1)]
    for _ in range(k) :
        value = 0
        for j in range(n) :
            value += zero[j]
            zero[j] = value
        
    print(zero[n-1])