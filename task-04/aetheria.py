
n = int(input())
l=list(map(int, input('').split()))
least = min(l)
if(l.count(least)>1):
    print('Still Aetheria')
else:
    print(l.index(least)+1)


