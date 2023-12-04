
t = int(input())

for _ in range(t):
    n = int(input())
    a = 1
    b = 2
    c = 0
    s= 2
    while c<=n:
        c = a + b
        a = b
        b = c
        if c%2 == 0 and c<=n:
            s+=c
    print(s)

