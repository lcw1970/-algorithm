a,b = map(int,input().split())

if a < b :
    a,b = b,a 

def gcd(a,b) :
    while b != 0 :
        a,b = b,a%b 
    return a

g = gcd(a,b)
l = a*b//g 
print(g)
print(l)
