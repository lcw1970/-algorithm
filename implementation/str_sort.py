# 내풀이
n = input()
lst = list(n)
lst.sort()
result= 0
indx = 0
for i in range(len(lst)) :
    if lst[i].isnumeric() :
        
        result += int(lst[i])
    
    else :
        indx = i
        break
# 개선된 풀이
for i in lst[indx:] :
    print(i,end="")
print(str(result))

n = input()
letters = []
total = 0

for c in n:
    if c.isdigit():
        total += int(c)
    else:
        letters.append(c)

letters.sort()
print(''.join(letters) + str(total))
