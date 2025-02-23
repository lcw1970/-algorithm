import sys 
input = sys.stdin.readline

arr = [0] * 1000001

n = int(input().strip())

for _ in range(n) :
    num = int(input().strip())
    arr[num] += 1

for i in range(1,10000001) :
    if arr[i] > 0 :
        for _ in range(arr[i]):
            print(i)

    