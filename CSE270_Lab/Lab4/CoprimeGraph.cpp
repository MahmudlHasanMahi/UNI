#include <iostream>
using namespace std;
#include<vector>


int GCD(int a, int b) {
    return b ? GCD(b, a % b) : a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;


    vector<vector<int>> g(n + 1);


    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (i != j && GCD(i, j) == 1) {
                g[i].push_back(j);
            }
        }
    }

    for (int j = 0; j < q; ++j) {
        int x, k;
        cin >> x >> k;

        if (k > g[x].size()) {
            cout << -1 << endl;
        }
        else {
            cout << g[x][k - 1] << endl;
        }
    }

    return 0;
}