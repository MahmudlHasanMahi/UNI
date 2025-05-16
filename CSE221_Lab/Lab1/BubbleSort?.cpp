#include <iostream>
#include <string>
using namespace std;

void bubble_sort(int *arr,int n){

    for (int i = 0; i < n - 1; i++) {

        bool flag= true;
        int j = 0;
        while(j < n - i-1){
            if(arr[j+1] < arr[j]){
                flag = false;
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
            j++;
        }
        if(flag){
            break;
        }
    }
}   

int main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i = 0; i < n ;i++){
        scanf("%d",&arr[i]);
    }
    bubble_sort(arr,n);
    for(int i : arr){
        cout<<i<<" ";
    }
    return 0;
}