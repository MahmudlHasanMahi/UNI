#include <iostream>
#include <string>
using namespace std;

int lower(int arr[], int t, int n) {
    int l = 0, r = n - 1;
    while (l <= r) {
        int m = (r + l) / 2;
        if (arr[m] >= t) {
            r = m - 1;
        }
        else {
            l = m + 1;
        }
    }
    return l;
}

int upper(int arr[], int t, int n) {
    int l = 0, r = n - 1;
    while (l <= r) {
        int m = (r + l) / 2;
        if (arr[m] <= t) {
            l = m + 1;
        }
        else {
            r = m - 1;
        }
    }
    return r;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    cin >> n >> k;
    int arr[n];

    for (int i = 0; i < n; i++) cin >> arr[i];
    while (k--) {
        int x, y;
        cin >> x >> y;
        int l = lower(arr, x, n);
        int r = upper(arr, y, n);
        cout << r - l + 1 << endl;

    }

}