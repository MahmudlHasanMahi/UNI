#include <iostream>
#include <string>
using namespace std;
int main(){
    int n,num;
    cin >> n;
    while(n--){
        scanf("%d",&num);
        if(num % 2 == 0){
            printf("%d is an Even number.\n",num);

        }else{
            printf("%d is an Odd number.\n",num);
        }
    }


}