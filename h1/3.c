#include <stdio.h>

//Zadacha 3

int main() {
    int x,y;
    int temp;
    int isPrime = 0;
    
    do{
        printf("Enter x: \n");
        scanf("%d", &x);
        printf("Enter y: \n");
        scanf("%d", &y);
    }while(x >= y);
    
    for(x = x; x <= y; x++) {
        for(temp = 2; temp < x; temp++) {
            if( x % temp == 0) {
                isPrime = 0;
                break;
            }else {
                isPrime = 1;   
            }
        }
        if(isPrime == 1) {
            if(x % 10 == 3) {
                printf("%d\n", x);
                isPrime = 0;  
            }   
        }
    }
    
    getch();
    return 0;
}
