lst = []

x = 0
for _ in range(3):
    a= input()
    lst.append(a)

for i in lst :
    if i.isdigit():
        x = int(i)+3-lst.index(i)
        
if x % 15 == 0:
    print("FizzBuzz")
elif x % 3 == 0 :
    print("Fizz")
elif x % 5 == 0 :
    print("Buzz")
else :
    print(x)