#include <iostream>
#include <string>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n,m;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)cin>>a[i];
    cin>>m;
    int b[m];
    for(int i=0;i<m;i++)cin>>b[i];
    int x=0,y=0;

    while(x < n && y < m){
        if(a[x] <= b[y]){
            cout<<a[x++]<<" ";
        }else{
            cout<<b[y++]<<" ";
        }
    }
    while(x < n){
            cout<<a[x++]<<" ";
    }
    while(y < m){
            cout<<b[y++]<<" ";
    }
    


    return 0;
}