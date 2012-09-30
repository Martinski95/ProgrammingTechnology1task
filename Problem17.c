#include <stdio.h>

//Zadacha 17

int isPrime(int num);

int main() {
    float x;
    float sum = 0.0;
    int i = 0;
    
    do{
        printf("Enter x(float): \n");
        scanf("%f", &x);
    }while(!((x > 0) && (x < 1)));
    
    while(1) {
        if(isPrime(i) && isPrime(i + 2)) {
            sum += 1.0/(float)i + 1.0/(float)(i+2);
            
            if((float)i / (float)(i + 2) < x) {
                break;   
            }
        }
        i++;
    }
    
    printf("Sum = %f", sum);
    
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
