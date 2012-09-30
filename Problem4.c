#include <stdio.h>

//Zadacha 4

int main() {
    int x,y;
    int temp = 1;
    int i = 0;
    
    do{
        printf("Enter x: \n");
        scanf("%d", &x);
        printf("Enter y: \n");
        scanf("%d", &y);
    }while(x >= y);
    
    while(temp < y) {
        i = x + temp;
        x = temp;
        temp = i;
        if(temp < y) {
            printf("%d\n", i);   
        }
    }
    
    getch();
    return 0;   
}
