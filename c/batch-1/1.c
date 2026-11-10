//Multiples of 3 or 5

//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//Find the sum of all the multiples of 3 or 5 below 1000.


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
