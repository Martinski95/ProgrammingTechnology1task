#include <stdio.h>

//Zadacha 7

int main() {
    int x;
    int arrLength = 10;
    float arr[arrLength];
    int count = 0;
    int i = 0;
    float temp;
    
    do{
        printf("Enter x: \n");
        scanf("%d", &x);
    }while(!((x > 0) && (x <= 10)));
    
    while(count < 10) {
        temp = cos(i);
        i++;
        if((int)(temp * 1000) % 10 == x) {
            arr[count] = temp;
            count++;
        }
        i++;
    }

    for(i = 1; i <= arrLength; i++) {
        printf("Element %d : %f\n", i, arr[i]);   
    }
    
    getch();
    return 0;   
}
