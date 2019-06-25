#include <stdio.h>
#include <math.h>

int factorial(int n){
    if (n==0){
        return 1;
    } else{
        return n*factorial(n-1);
    }
}

int permutation(int n, int k){
    return factorial(n)/factorial(n-k);
}


int birthdayParadox(n){
    int total_cases = pow(365, n);
    float permutations = permutation(365, n);

    return (1 - (permutations/total_cases));
}


int main(){
    float n;
    scanf("%f", &n);
    printf("%f", birthdayParadox(n));
}