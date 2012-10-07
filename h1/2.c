#include <stdio.h>

/*
ТУЕС
11 А
17
Мартин Красимиров Кирилов
Да се разработи програма, която изисква от потребителя да въведе две целочислени числа, x и y, 
където x < y. Да се намери и изведе сумата на числата делящи се на 17 в интервал [x, y].
*/

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
        if(x % 17 == 0) {
            sum += x;
        }
    }
    
    printf("Sume = %d\n", sum);
    getch();
    return 0;
}
