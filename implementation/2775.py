n = int(input())

def fact(x):
    if x <= 1 :
        return 1
    return x*fact(x-1)

result = fact(n)
result = list(map(int,str(result)))

count =0 
for i in result[::-1]:
    if i != 0 :
        break
    count +=1
print(count)