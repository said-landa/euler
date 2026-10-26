#include <stdio.h>
#include <stdlib.h>

int sum(int *arr, size_t len) {
    int sumA = 0;
   
    for (size_t i = 0; i < len; i++) {
        sumA += arr[i];
    }

    return sumA;
}

int main(void) {
    int number = 1000;
    int m1 = 3;
    int m2 = 5;
    size_t capacity = 2;
    size_t size = 0;

    int *arrM = malloc(capacity * sizeof(int));
    if (arrM == NULL) { return 1;}

    for (int i = 1; i < number; i++) {
        if (i % m1 == 0 || i % m2 == 0) {
            if (size == capacity) {
                size_t newCapacity = capacity * 2;

                int *temp = realloc(arrM, newCapacity * sizeof *arrM);
                if (temp == NULL) {
                    free(arrM); 
                    return 1;
                }

                arrM = temp;
                capacity = newCapacity;
            }

            arrM[size] = i;
            size++;
        }
    }

    int res = sum(arrM, size);
    printf("%d\n", res);

    free(arrM);
    return 0;
}