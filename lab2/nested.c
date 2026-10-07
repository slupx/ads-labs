#include <stdio.h>

#define SQRT_2 1.4142135623730951

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    double x = 2.0;
    double res = SQRT_2;
    double s;
    double num = (1.0 + x) * (1.0 + x); // precompute (1+x)^2

    unsigned long long ops = 0;
    ops += 6; // init: x, res, num (add+mul+assign), ops

    for (int i = 1; i <= n; ++i) {
        ops += 1; // i <= n
        s = 0.0;
        ops += 1; // s = 0
        ops += 1; // j = 1

        for (int j = 1; j <= i; ++j) {
            ops += 1; // j <= i
            s += 4.0 * j - 1.0;
            ops += 3; // mul, sub, +=
            ops += 1; // ++j
        }
        ops += 1; // final j <= i

        res *= 1.0 - num / (4.0 * s);
        ops += 4; // 4*s, /, 1-, *=
        ops += 1; // ++i
    }
    ops += 1; // final i <= n

    printf("Result:     %.7f\n", res);
    printf("Operations: %llu\n", ops);

    return 0;
}