#include <iostream>
using namespace std;

void print_using_recursion(int n)
{
    if (n == 0)        // Base case
        return;

    cout << n << endl; // Work

    print_using_recursion(n - 1); // Recursive call
}

int main()
{
    int n;
    cout << "Enter the number: ";
    cin >> n;

    print_using_recursion(n);

    return 0;
}
