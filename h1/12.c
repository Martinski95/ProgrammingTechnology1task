#include <stdio.h>

//Zadacha 12

int main() {
    int x;
    int arr[10];
    int sum = 0;
    int currN = 1;
    int i, j;
    int N = 1;
    
    
    do {
        printf("Enter x : \n");
        scanf("%d", &x);   
    }while(!(x > 0) && (x < 10));
    
    for(i = 0; i < 10; i++) {
        while(1) {
            ++N;
            if((N % x == 0) && (N > currN)) {
                for(j = 0; j <= N; j++) {
                    sum += j;
                    currN = N;  
                }
                arr[i] = sum;
                sum = 0;
                break;
                
            }
            
        }
    }
    
    for(i = 0; i < 10; i++) {
    printf("Arr[%d] = %d\n", i+1, arr[i]);   
    }
    
    getch();
    
    return 0;
}
