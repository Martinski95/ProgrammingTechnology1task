#include <stdio.h>

//Zadacha 11

int main() {
    int x;
    float arr[10];
    int i;
    int N;
    float sum;
    
    do {
        printf("Enter x : \n");
        scanf("%d", &x);   
    }while(!((x > 0) && (x < 10)));
    
    for(N = 0; N < 10; N++) {
        sum = 0.0;
        
        for(i = N*x; i < (N+1)*x; i++) {
            sum += cos(i);
        }
        
        arr[N] = sum;
    }
    
    for(i = 0; i < 10; i++) {
        printf("Arr[%d] = %f\n", i+1, arr[i]);
    }
    
    getch();
    
    return 0;   
}
