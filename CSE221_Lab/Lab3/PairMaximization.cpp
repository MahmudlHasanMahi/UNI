#include <iostream>
#include <string>
using namespace std;

long long merge(long long arr[], int l, int m, int r) {
    float inf = -1 * numeric_limits<float>::infinity();
    long long x = inf, y = inf;
    for (int i = l; i <= m;i++) x = max(x, arr[i]);
    for (int i = m + 1; i <= r;i++) y = max(y, arr[i] * arr[i]);
    return x + y;
}


long long mergeSort(long long arr[], int l, int r) {
    if (l >= r) return -1 * numeric_limits<float>::infinity();
    if (l + 1 == r) return arr[l] + arr[r] * arr[r];
    int mid = (l + r) / 2;
    long long left = mergeSort(arr, l, mid);
    long long right = mergeSort(arr, mid + 1, r);
    long long cross = merge(arr, l, mid, r);
    return max(max(left, right), cross);
}

long long  PairMaximization(long long arr[], int n) {
    return mergeSort(arr, 0, n - 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    long long arr[n];
    for (int i = 0; i < n;i++)cin >> arr[i];

    cout << PairMaximization(arr, n);


}