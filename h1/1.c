#include <stdio.h>

//Zadacha 1

int main() {
    int x,y;
    int sum = 0;
    
    do{
        printf("Enter x: \n");
        scanf("%d", &x);
        printf("Enter y: \n");
        scanf("%d", &y);
    }while(x >= y);
    
    for(x = x; x <= y; x++) {
        if(x % 2 != 0) {
            sum += x;
        }
    }
    
    printf("Sume = %d\n", sum);
    getch();
    return 0;   
}
