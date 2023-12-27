#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

long long solution(int r1, int r2) {
    long long r,l,result=0;
    for(int i=0; i<r2+1; i++){
        l=floor(sqrt(pow(r2,2)-pow(i,2)));
        r=(i<=r1)?ceil(sqrt(pow(r1,2)-pow(i,2))):0;
        result+=l-r+1;
    }
    return result*4-4*(r2-r1+1);
}
