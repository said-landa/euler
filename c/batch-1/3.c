//Largest Prime Factor

//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143?

#include <stdio.h>
#include <math.h>
#include <inttypes.h>

int64_t divide(int64_t n, int i) {
    while (n % i == 0) {
        n = n / i;
    }
    return n;
}

int main(void) {
    int64_t num = 600851475143;
    int i = 2;

    while (i <= sqrt((double)num)) {
        if (num % i == 0) {
            num = divide(num, i);
        }
        i++;
    }
    
    printf("%" PRId64 "\n" , num);

    return 0;
}
