#include <stdio.h>

//Zadacha 8

int main() {
    int x,i;
    int arrLength = 10;
    int arr[arrLength];
    int temp = 0;
    int a = 0;
    int b = 1;
    int next;
    
    do{
        printf("Enter x: \n");
        scanf("%d", &x);
    }while(!((x > 0) && (x <= 10)));
    
    
    do{
        next = b;
        b = b + a;
        a = next;
        
        if(b % x == 0) {
            temp++;
            arr[temp] = b;   
        }
    }while(temp < 10);

    for(i = 1; i <= arrLength; i++) {
        printf("Element %d : %d\n", i, arr[i]);   
    }
    
    getch();
    return 0;   
}
