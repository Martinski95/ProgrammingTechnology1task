#include <stdio.h>

//Zadacha 9

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
