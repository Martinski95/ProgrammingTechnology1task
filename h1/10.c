/*
Технологично училище „Електронни системи” http://www.elsys-bg.org/
11 А
17
Мартин Красимиров Кирилов
Да се разработи програма,  която изисква от потребителя да въведе четири числа x, y, w, h, 
където x>0, y>0, w>0, h>0. Числото x е дължината на плоча дървесина, а числото y е височината. 
Да се определи на колко цели плочи с размери w, h може да се разреже голямата плоча. 
Да се инициализира масив от 10 елемента. Стойностите на елементите на масива да са първите 
10 координати по дължина на плочата, в които тя трябва да се разреже, за да се получат по-малките плочи.
*/

#include <stdio.h>

int main() {
    float x;
    float y;
    float w;
    float h;
    int kWidth;
    int kHeight;
    int num;
    float arr[10];
    int i;
    float coord = 0;
    
    do {
        printf("Enter x : \n");
        scanf("%f", &x);
    }while(x <= 0);
    
    do {
        printf("Enter y : \n");
        scanf("%f", &y);
    }while(x <= 0);

    do {
        printf("Enter w : \n");
        scanf("%f", &w);
    }while(x <= 0);
    
    do {
        printf("Enter h : \n");
        scanf("%f", &h);
    }while(x <= 0);
    
    kWidth = x / w;
    kHeight = y / h;
    num = kWidth * kHeight;
    
    printf("kWidth = %d, kHeight = %d, num = %d\n", kWidth, kHeight, num);
    
    if(kWidth > 0) {
        for(i = 0; i < kWidth; i++) {
            coord += w;
            arr[i] = coord;
            printf("Coordinate %d : %f\n", i+1, arr[i]);  
        }   
    }
    
    getch();
    return 0;
}
