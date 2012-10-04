#include <stdio.h>

//Zadacha 15

int main() {
    int x;
    long long arr[10];
    int N;
    int i;
    long long first = 1;
    long long second = 1;
    long long next;
    
    do {
        printf("Enter x : \n");
        scanf("%d", &x);   
    }while(!((x > 0) && (x < 10)));
    
    for(N = 0; N < 10; N++) {
        while(1) {
            next = first + second;
            first = second;
            second = next;
            if(second % 10 == x) {
                arr[N] = second;
                break;
            }
        }
    }
    
    for(i = 0; i < 10; i++) {
        printf("Arr[%d] = %d\n", i+1, arr[i]);   
    }
    
    getch();
    
    return 0;   
}
