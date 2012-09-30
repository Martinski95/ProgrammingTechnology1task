#include <stdio.h>

//Zadacha 14

int isPrime(int num);

int main() {
    int x;
    int arr[10];
    int N;
    int i = 3;
    int cyc = 1;
    
    do {
        printf("Enter x : \n");
        scanf("%d", &x);   
    }while(!((x > 0) && (x < 10)));
    
    for(N = 0; N < 10; N++) {
        cyc = 1;
        while(cyc) {
            i++;
            if(isPrime(i)) {
                if(i % 10 == x) {
                    arr[N] = i;
                    cyc = 0;
                }   
            }
        }
        
    }
    
    for(i = 0; i < 10; i++) {
    printf("Arr[%d] = %d\n", i+1, arr[i]);   
    }
    
    getch();
    
    return 0;
}

int isPrime(int num) {
    int i, n;
    int isPr;
    for(i = 3; i <= num; i++) {
        isPr = 1;
        for(n = 2; n < i; n++) {
            if(i % n == 0){
                isPr = 0;
            } 
        }
    }
    return isPr;
}
