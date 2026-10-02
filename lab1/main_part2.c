#include <stdio.h>

int main() {
  double x, y;

  printf("Enter x: ");
  scanf("%lf", &x);
  
  if ((x >= -32 && x < -20) || x > 10) {
    y = x * x - 3;
    printf("%g\n", y);
  } else {
    if (x > 0 && x <= 5) {
      y = x * x * (x - 5);
      printf("%g\n", y);
    } else {
      printf("No rule for given x\n");
    } 
  }
  
  return 0;
}