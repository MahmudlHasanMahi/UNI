#include <iostream>
#include <string>
using namespace std;

long long merge(long long arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;long long c = 0;
    int a[n1], b[n2];
    for (int i = 0; i < n1;i++) a[i] = arr[l + i];
    for (int i = 0; i < n2;i++) b[i] = arr[m + i + 1];
    int j = 0, k = 0, n = l;
    while (j < n1 && k < n2) {
        if (a[j] < b[k]) {
            arr[n++] = a[j++];
        }
        else {
            arr[n++] = b[k++];
            c += n1 - j;
        }
    }
    while (j < n1) {
        arr[n++] = a[j++];
    }
    while (k < n2) {
        arr[n++] = b[k++];
    }
    return c;
}

long long mergeSort(long long arr[], int l, int r) {
    long long c = 0;
    if (l < r) {
        int m = (l + r) / 2;
        c += mergeSort(arr, l, m);
        c += mergeSort(arr, m + 1, r);
        c += merge(arr, l, m, r);

    }
    return c;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n;
    cin >> n;
    long long arr[n];
    for (int i = 0; i < n;i++)cin >> arr[i];

    cout << mergeSort(arr, 0, n - 1) << endl;
    for (int i : arr) {
        cout << i << " ";
    }

}