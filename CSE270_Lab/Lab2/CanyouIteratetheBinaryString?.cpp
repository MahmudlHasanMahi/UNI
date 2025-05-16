#include <iostream>
#include <string>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        string str;
        cin>>str;

        int l = 0,r = str.length()-1;

        while(l < r && str[0] != '1'){
            int mid = (l+r)/2;
            // printf("%d %d\n", l,r);
            if(str[mid] == '1'){
                r = mid;
            }else{
                l = mid+1;
            }
        }
        if(str[0] == '1'){
            cout<<1<<endl;
        }else if(str[l] == '0'){
            cout<<-1<<endl;
        }else{
            cout<<l+1<<endl;
        }


    }
 


    return 0;
}