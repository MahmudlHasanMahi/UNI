#include <iostream>
#include <string>
using namespace std;



int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, t, c = 0, ts = 0, x = 0;
    cin >> n >> t;
    int arr[n];
    for (int i = 0; i < n;i++)cin >> arr[i];
    for (int i = 0; i < n;i++) {
        ts += arr[i];
        while (ts > t) {
            ts -= arr[x];
            x++;
        }
        c = max(c, i - x + 1);
    }

    cout << c << endl;

}
