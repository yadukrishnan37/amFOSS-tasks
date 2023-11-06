
#include <stdio.h>

int is_prime(int x)
{
    int count=0;
    for(int i=1; i<=x;i++)
    {
        if(x%i==0)
            count++;
    }
    return count==2?1:0;
}

int main()
{
    int n;
    printf("Enter the limit: ");
    scanf("%d", &n);
    for(int i=2; i<=n;i++)
    {
        if(is_prime(i)==1)
            printf("%d ", i);
    }
}

