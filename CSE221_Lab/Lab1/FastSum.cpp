#include <iostream>
#include <string>
using namespace std;
int main(){
    int n ;
    long long k,j;
    scanf("%d",&n);
    while(n--){
        scanf("%lld",&k);
        j = k*(1+k)/2;
        printf("%lld\n", j);
    }

    return 0;
}