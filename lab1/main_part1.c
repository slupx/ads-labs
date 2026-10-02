#include <stdio.h>

int main() {
  double x, y;
  int is_defined;

  printf("Enter x: ");
  scanf("%lf", &x);

  is_defined = 0;
  
  if (x > 10) {
    y = x * x - 3;
    is_defined = 1;
  } else {
    if (x < -20) {
      if (x >= -32) {
        y = x * x -3;
        is_defined = 1;
      }
    } else {
      if (x > 0) {
        if (x <= 5) {
          y = x * x * (x - 5);
          is_defined = 1;
        }
      }
    }
  } 

  if (is_defined == 1) {
    printf("%g\n", y);
  } else {
    printf("No rule for given x\n");
  }

  return 0;
}