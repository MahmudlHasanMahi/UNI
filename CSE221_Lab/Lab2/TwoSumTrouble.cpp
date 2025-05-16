#include <iostream>
#include <string>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int n,t;
    cin>>n>>t;
    int arr[n];

    for(int i=0;i<n;i++) cin>>arr[i];
    bool flag = false;
    int l = 0,r = n-1;

    while(l < r){
        int s = arr[l] + arr[r];
        if(s == t){
            cout<<++l<<" "<<++r<<endl;
            flag = true;
            break;
        }
        else if(s > t){
            r--;
        }else{
            l++;
        }
    }
    if(!flag){
        cout<<-1<<endl;
    }
    
    return 0;
}