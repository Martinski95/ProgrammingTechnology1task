#include <stdio.h>

//Zadacha 10

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
