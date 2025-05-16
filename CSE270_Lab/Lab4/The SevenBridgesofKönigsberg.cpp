#include <iostream>
using namespace std;
#include<vector>

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int v, e;

    cin >> v >> e;

    int odd = 0, even = 0;
    vector<int> arr(v, 0);
    for (int i = 0; i < 2 * e;i++) {
        int x;
        cin >> x;;
        arr[x - 1]++;
    }
    for (int i = 0;i < v;i++) {
        if (arr[i] % 2 == 0) even++;
        else odd++;

    }
    if (even == v || odd == 2){
        cout<< "YES"<<endl;
    }else{

        cout<< "NO"<<endl;
    }




        return 0;
}