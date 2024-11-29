//https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/cpp
#include <string>

std::string reverse_words(std::string str) {
  std::string reverse_text = "";

  for (unsigned int i = 0; i < str.length(); ++i)
    reverse_text += str;
  
  return reverse_text;
}

int main(void) {
  printf("%s", reverse_words("awd"));
}
