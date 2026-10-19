#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int number = 1000;
    int m1 = 3;
    int m2 = 5;
    int capacity = 2;
    int size = 0;

    int *arrM = malloc(capacity * sizeof(int));
    if (arrM == NULL) { return 1;}

    for (int i = 1; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            if (size == capacity) {
                capacity *= 2;

                int *temp = realloc(arrM, capacity * sizeof(int));
                if (temp == NULL) {
                    free(arr); 
                    return 1;
                }

                arrM = temp;
            }

            arrM[i - 1] = i;
        }
    }

    

   
    free(arr);
    return 0;
}