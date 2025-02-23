n , k =map(int,input().split())
coins = [int(input() for _ in range(n))]
count = 0

coins.sort(reverse=True)

for coin in coins :
     if k == 0:  # 최적화 포인트
        break
     if coin <= k:
        count += k //coin
        k %= coin
print(count)
