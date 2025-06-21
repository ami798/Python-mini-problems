#include <iostream>
using namespace std;

void tricky(int n) {
    if (n <= 0) return;
    tricky(n - 1);
    cout << n << " ";
    tricky(n - 2);
}

int main() {
    tricky(3);
    return 0;
}