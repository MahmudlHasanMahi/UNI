#include <iostream>
using namespace std;
#include<vector>

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    int g, x, y, m = 0;
    cin >> g >> x >> y;

    vector<vector<int>> v;

    int i = max(1, x - 1);
    while (i <= x + 1 && i <= g) {
        int j = max(1, y - 1);
        while (j <= y + 1 && j <= g) {
            if (i != x || j != y) v.push_back({ i, j });
            j++;
        }
        i++;
    }
    cout << v.size() << endl;
    for (auto a : v) {
        cout << a[0] << ' ' << a[1] << endl;

    }

    return 0;
}