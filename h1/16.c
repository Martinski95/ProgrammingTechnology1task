/*
Технологично училище „Електронни системи” http://www.elsys-bg.org/
11 А
17
Мартин Красимиров Кирилов
Да се разработи програма, която изисква от потребителя да въведе целочислено число x, 
където x e интервала [0; +∞). Да се намерят първите 10 нечетни числа делители на x и да се запишат в масив. 
Масивът да се изведе на екрана и да се намерят простите числа в този масив.
*/

#include <stdio.h>

int isPrime(int num);

int main() {
    int x;
    long long arr[10];
    int i = 1;
    int N = 0;
    
    do {
        printf("Enter x : \n");
        scanf("%d", &x);   
    }while(x < 0);
    
    for(N = 0; N < 10; N++) {
        while(1) {
            if(x % i == 0) {
                arr[N] = i;
                printf("Arr[%d] = %d\n", N+1, arr[N]);
                if(isPrime(arr[N])) {
                    printf("%d is prime\n", arr[N]);
                }
                i += 2;
                break;
            }
            i += 2;
        }
    }
    
    getch();
    
    return 0;
}

int isPrime(int num) {
    int i, n;
    int isPr;
    for(i = 3; i <= num; i++) {
        isPr = 1;
        for(n = 2; n < i; n++) {
            if(i % n == 0){
                isPr = 0;
            } 
        }
    }
    return isPr;
}
