#include <stdio.h>

int main() {
    int a = 5;
    int *p = &a;
    int **q = &p;

    printf("Value of a: %d\n", **q);
    printf("Address of a: %p\n", (void *)p);
    printf("Address of pointer p: %p\n", (void *)q);

    return 0;
}
