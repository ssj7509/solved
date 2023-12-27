#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
bool solution(const char* s) {
    int n[]={0,0};
    for(int i=0; i<strlen(s); i++){
        n[s[i]==')']++;
        if (n[1]>n[0]) return 0;
    }
    return n[0]==n[1];
}