#include <iostream>
using namespace std;

int power(int x, int y)
{
    if (y == 0)
        return 1;

    return x * power(x, y - 1);
}

int main()
{
    int x, y;

    cout << "Enter base: ";
    cin >> x;

    cout << "Enter exponent: ";
    cin >> y;

    cout << "Answer = " << power(x, y);

    return 0;
}
