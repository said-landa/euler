#include <stdio.h>

int main(void) {
    int a = 1; int b = 2; int c = 0;
    int sumEven = 2;

    while (c < 4000000) {
        c = a + b;
        a = b;
        b = c;
        if (c % 2 == 0) {
        sumEven += c;
    }
    }

    printf("%d\n", sumEven);

    return 0;
}