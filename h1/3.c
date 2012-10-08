/*
Технологично училище „Електронни системи” http://www.elsys-bg.org/
11 А
17
Мартин Красимиров Кирилов
Да се разработи програма, която изисква от потребителя да въведе две целочислени числа, x и y, 
където x < y. Да се намерят и изведат всички прости числа завършващи на 3 в интервал [x,y].
*/

#include <stdio.h>

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
