/*
Технологично училище „Електронни системи” http://www.elsys-bg.org/
11 А
17
Мартин Красимиров Кирилов
Да се разработи програма, която изисква от потребителя да въведе две целочислени числа, x и y, 
където x < y. Да се намери сумата на всички нечетни числа в интервала [x,y].
*/
#include <stdio.h>

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
    
    printf("Sum = %d\n", sum);
    getch();
    return 0;   
}
