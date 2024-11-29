//https://www.codewars.com/kata/526571aae218b8ee490006f4/train/c
#include <stddef.h>
#include <stdio.h>

size_t countBits(unsigned value) {
  size_t bit_sum = 0;
  for (unsigned int i = 0; i < 32; ++i)
    if (value&(1<<i)) ++bit_sum;
  return bit_sum;
}

int main(void) {
  printf("1234: %u\n", countBits(1234)); //5
  printf("7: %u\n", countBits(7)); //5
  printf("77231418: %u\n", countBits(77231418)); //5
  printf("3811: %u\n", countBits(3811)); //5
}
