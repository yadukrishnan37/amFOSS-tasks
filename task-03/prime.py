
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return 1
    else:    
        return 0

print('Enter the limit: ')
n=int(input())
for i in range(2,n+1):
    if prime(i)==1:
        print(i,end=' ')
print('\n')
