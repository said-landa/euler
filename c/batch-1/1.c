#include <stdio.h>

int main(void) {
    int number = 1000; int sumA = 0; int m1 = 3; int m2 = 5; 

    for (size_t i = 0; i < number; i++) {
        if (i % m1 == 0 || i % m2 == 0) {
            sumA += i;
        }
    }

    printf("%d\n", sumA);
    return 0;
}
