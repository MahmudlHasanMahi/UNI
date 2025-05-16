#include <iostream>
using namespace std;
#include<vector>

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int v;

    cin >> v;
    vector<vector<int>> arr(v, vector<int>(v, 0));
    for (int i = 0; i < v; i++) {
        int x;
        cin >> x;
        while (x--) {
            int e;
            cin >> e;
            arr[i][e] = 1;

        }

    }
    for (int i = 0; i < v;i++) {
        for (int j = 0; j < v;j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }

    return 0;
}
