#include <stdio.h>

//Zadacha 13

int main() {
    int x;
    int arr[10];
    int sum = 0;
    int N = 1;
    int i;
    
    do {
        printf("Enter x : \n");
        scanf("%d", &x);   
    }while(!(x > 0) && (x < 10));
    
    for(N = 0; N < 10; N++) {
        sum = 0;
        for(i = 0; i < 1000; i++) {
            if(i % ((N+1)*x) == 0) {
                sum += i;   
            }   
        }
        arr[N] = sum;
    }
    
    for(i = 0; i < 10; i++) {
    printf("Arr[%d] = %d\n", i+1, arr[i]);   
    }
    
    getch();
    
    return 0;
}

