#include <iostream>
using namespace std;

int main() {
    int a = 1, b = 2, c = 3, d = 4, e = 5, f = 6, g = 7, h = 8, i = 9, j = 10;
    int result = 0;

    if (a > b) {
        if (c < d) {
            result = a + c;
        } else {
            if (e == f) {
                result = b + d;
            } else {
                for (int k = 0; k < 10; k++) {
                    if (k % 2 == 0) {
                        result += k;
                    } else {
                        result -= k;
                    }
                }
            }
        }
    } else {
        switch (g) {
            case 1:
                result = h + i;
                break;
            case 2:
                result = i - j;
                break;
            default:
                for (int m = 0; m < 5; m++) {
                    for (int n = 0; n < 5; n++) {
                        result += m * n;
                    }
                }
                break;
        }
    }

    cout << "Result: " << result << endl;
    return 0;
}