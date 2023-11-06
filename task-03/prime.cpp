
#include <iostream>

bool is_prime(int x)
{
    int count = 0;
    for(int i=1; i<=x;i++)
    {
        if(x%i==0)
            count++;
    }
    if(count == 2)
        return true;
    else
        return false;
}

int main() {
    int num;
    std::cout << "Enter the limit: ";
    std::cin >> num;

    for(int i=2; i<=num;i++)
    {
        if(is_prime(i)==true)
            std::cout<< i << std::endl;
    }
    return 0;
}



