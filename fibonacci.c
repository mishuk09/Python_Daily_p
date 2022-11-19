#include <stdio.h>
int main()
{

    int i, n1 = 0, n2 = 1, n3, n;
    printf("Enter the number that you want=");
    scanf("%d", &n);

    for (i = 2; i < n; ++i)
    {
        printf("Fibonacci is %d \n", n3);

        n1 = n2;
        n2 = n3;
        n3 = n1 + n2;
    }
    return 0;
}