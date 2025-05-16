#include <iostream>
using namespace std;
#include<vector>

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int v, e;

    cin >> v >> e;
    vector<int> arr(v, 0);
    
    for (int i = 0; i < e;i++) {
        int x;
        cin >> x;

        arr[x - 1]--;
    }

    for (int i = 0; i < e;i++) {
        int x;
        cin >> x;

        arr[x - 1]++;
    }

    for (int i = 0; i < v;i++) {
        cout<<arr[i]<<" ";
    }
    return 0;
}
