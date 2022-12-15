
#include <stdio.h>
int main()

{

    int i, n, count = 0;
    printf("enter any number=");
    scanf("%d", &n);

    for (i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            count++;
            break;
        }
    }

    if (count == 0)
    {
        printf("Prime number ");
    }
    else
        printf("not prime");
    return 0;
}