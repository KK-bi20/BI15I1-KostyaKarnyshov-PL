#include <iostream>

int main() {
    int array[] = { 1, 2, 3, 4, 5 };
    int* begin = array;
    int* end = array + sizeof(array) / sizeof(*array) - 1;

    while (begin < end) {
        *begin ^= *end ^= *begin ^= *end;
        begin++; end--;
    }

    for (const int* p = array; p < array + sizeof(array) / sizeof(*array); p++) {
        std::cout << *p << " ";
    }
}