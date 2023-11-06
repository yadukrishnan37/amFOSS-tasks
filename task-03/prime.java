

import java.util.*;

class foss
{
    public static void main(String args[]) 
    {
        Scanner sc = new Scanner(System.in);
        check prime = new check();
        System.out.println("Enter the limit: ");
        int n = sc.nextInt();
        for(int i = 2; i <= n; i++) 
        { 
            if (prime.isPrime(i) == 1)
                System.out.print(i + " ");
        }
        sc.close();
    }
}
class check 
{
    int isPrime(int x) 
    {
        int count = 0;
        for(int i = 1; i <= x; i++) 
        { 
            if (x % i == 0)
                count++;
        }
        if(count == 2)
            return 1;
        else
            return 0;
    }
}
