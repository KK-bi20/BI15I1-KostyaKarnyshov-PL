#include <iostream>
using namespace std;


unsigned long long fibonacci(unsigned long n)

{

    if (n == 0)
        return 0;

    if (n == 1)
        return 1;


    return fibonacci(n - 1) + fibonacci(n - 2);

}


int main()

{

    for (int count = 0; count < 50; ++count)
        cout << fibonacci(count) << " ";


    return 0;

}