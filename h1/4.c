#include <stdio.h>

/*
ТУЕС
11 А
17
Мартин Красимиров Кирилов
Да се разработи програма, която изисква от потребителя да въведе две целочислени числа, x и y, 
където x < y. Да се намерят и изведат всички числа на Фибоначи в интервала [x, y].
*/

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
