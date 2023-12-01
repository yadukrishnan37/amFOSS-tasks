
n = int(input())
construct = []

for i in range(n):
    l=list(map(int, input('').split()))
    construct.append(l)

sum = []

for i in range(3):
    s=0
    for j in range(n):
        s=s+construct[j][i]
    sum.append(s)    

if all(x==0 for x in sum):
    print("YES")
else:
    print("NO")


