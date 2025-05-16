#include <iostream>
#include <string>
using namespace std;

void bst(int arr[], int l, int r) {
    if (l <= r) {
        int mid = (l + r) / 2;
        cout << arr[mid] << " ";
        bst(arr, l, mid - 1);
        bst(arr, mid+1, r);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n;i++)cin >> arr[i];
    bst(arr, 0, n - 1);

}
