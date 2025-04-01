#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *maskify (char *masked, const char *string) {
  int str_length = strlen(string);
  unsigned i = 0;
  for (; i < str_length-4 && !(str_length-4 < 0); ++i)
    masked[i] = '#';
  for (; i < str_length; ++i)
    masked[i] = string[i];
  masked[strlen(string)] = '\0';
  return masked;
}

int main(void) {
  char* masked = malloc(32);
  const char* string = "3123123123";

  maskify(masked, string);
  
  printf("%s\n", masked);
}
