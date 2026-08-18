#include <stdio.h>

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int *s = a;

    printf("Forward: ");
    for (int i = 0; i < 5; i++)
        printf("%d ", *(s + i));

    printf("\nReverse: ");
    for (int i = 4; i >= 0; i--)
        printf("%d ", a[i]);

    return 0;
}
