

n = int(input())
s = 'amfoss'
l = []
c = []
for i in range(n):
    x = input()
    l.append(x)
for i in range(n):
    count = 0
    for j in range(6):
        if ord(l[i][j]) != ord(s[j]):
            count+=1
    c.append(count)

for i in range(n):
    print(c[i])