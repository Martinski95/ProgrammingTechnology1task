/*
Технологично училище „Електронни системи” http://www.elsys-bg.org/
11 А
17
Мартин Красимиров Кирилов
Да се разработи програма, която изисква от потребителя да въведе целочислено число x, 
където 0<x<10. Да се инициализира масив от 100 целочислени елемента. 
Стойностите на елементите да са случайни числа в интервала [0, 100). 
Елементите на масива да се подредят така, че числата завършващи на x да са в началото.
*/

#include <stdio.h>
#include <time.h>

int RandInt(int min, int max);

int main() {
    int x;
    int arrLength = 100;
    int arr[arrLength];
    int i,j;
    int count = 0;
    int temp;
    
    srand(time(0));
    
    do{
        printf("Enter x: \n");
        scanf("%d", &x);
    }while(!((x > 0) && (x < 10)));
    
    for(i = 0; i < arrLength; i++) {
        arr[i] = RandInt(0, 99);
    }

    for(i = 0; i < arrLength; i++) {
        if(arr[i] % 10 == x) {
            temp = arr[count];
            arr[count] = arr[i];
            arr[i] = temp;
            count++;   
        }   
    }

    for(i = 0; i < arrLength; i++) {
        printf("After sort element %d : %d\n", i+1, arr[i]);   
    }
    
    getch();
    return 0;   
}

int RandInt(int min, int max) {
    return min + rand()%(max - min + 1);
}
