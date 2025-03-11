n = int(input())
dic = {}
for _ in range(n):
    num = int(input())
    if num in dic :
        dic[num] += 1
    else :
        dic[num] = 1

max_num = max(dic.keys(),key=lambda x: (dic[x],-x ))
print(max_num)