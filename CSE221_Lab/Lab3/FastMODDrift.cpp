#include <iostream>
#include <string>
using namespace std;

long long modularExponent(long long a, long long b, int c) {
    if (b == 0)return 1;
    long long x = modularExponent(a, b / 2, c);
    x = x * x % c;
    if (b % 2 == 1) return x * a % c;

    return x;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long a, b;
    cin >> a >> b;
    cout << modularExponent(a, b, 107);


}

 