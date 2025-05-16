#include <iostream>
#include <string>
using namespace std;




void bubble_sort( int* a,int* b, int n,int &s){
    
    for(int i = 0; i < n;i++){
        int j = i+1;
        int k = i;
        while(j < n){
            if(a[j] > a[k]){
                k = j;
            }else if(a[j] == a[k] && b[j] < b[k]){
                k = j;
            }
            j++;
        }
        if(i != k){
            swap(a[k],a[i]);
            swap(b[k],b[i]);
            s++;
        
        }
    }

    
}

int main(){
    int n,s=0;
    scanf("%d",&n);
    int a[n],b[n];

    for(int i = 0 ; i < n; i++)
        scanf("%d",&b[i]);

    for(int i = 0 ; i < n; i++)
        scanf("%d",&a[i]);

    bubble_sort(a,b,n,s);


    printf("Minimum swaps: %d\n", s);
    for(int i = 0 ; i< n; i++){
        printf("ID: %d Mark: %d\n", b[i],a[i]);
    }

    return 0;
}