/*
Технологично училище „Електронни системи” http://www.elsys-bg.org/
11 А
17
Мартин Красимиров Кирилов
Да се разработи програма, която изисква от потребителя да въведе число x, където 0<x<1. 
Да се намери числото пи чрез следното развитие в ред:
4-4/3+4/5-4/7+4/9-4/11+...4/N. Развитието в ред спира при 4/N<x. 
Получената стойност за пи да се изведе на екрана.
*/

#include <stdio.h>

int main() {
    float x;
    float i = 4.0;
    float pi;
    float del = 1.0;
    int temp;
    int bool = 0;

    do{
        printf("Enter x(float): \n");
        scanf("%f", &x);
    }while(!((x > 0) && (x < 1)));
    
    for(del = 1.0; i / del > x; del += 2.0) {
        if(bool == 0) {
            pi -= i/del;
            bool = 1; 
        }else {
            pi += i/del;
            bool = 0;
        }
    }
    
    printf("Pi = %f\n", pi);
    
    getch();
    return 0;   
}
