#include <stdio.h>
#include <math.h>

//Zadacha 5

int main() {
    int x;
    int arrLength = 10;
    float arr[arrLength];
    int i,j;
    float temp;
    
    do{
        printf("Enter x: \n");
        scanf("%d", &x);
    }while(!((x > 0) && (x < 10)));
    
    for(i = 0; i < arrLength; i++) {
        arr[i] = cos(i);
        printf("Before sort element %d : %f\n", i+1, arr[i]);
    }
    
    //sorting
    for(i = 0; i < (arrLength - 1); i++) {
        for(j = (i + 1); j < arrLength; j++) {
            if(arr[i] < arr[j]) {
                   temp = arr[i];
                   arr[i] = arr[j];
                   arr[j] = temp;
            }   
        }   
    }
    
    for(i = 0; i < arrLength; i++) {
        printf("After sort element %d : %f\n", i+1, arr[i]);   
    }
    
    getch();
    return 0;   
}
