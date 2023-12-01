

def snint(a):
    minimum = 0
    for x in range(0,len(a)):
        if minimum == x and x in a:
            minimum += 1
    return minimum

t = int(input())
test = 0
ans=[]
while test < t:
    n = int(input())
    l = list(map(int, input().split()))
    
    maximum = 0
    for k in range(n):
        a=snint(l[0:k])
        b=snint(l[k:n])
        if (a+b)>maximum:
            maximum=a+b
    ans.append(maximum)
    test+= 1
for i in ans:
    print(i)

