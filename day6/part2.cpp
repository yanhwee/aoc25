#include <iostream>
#include <vector>

using std::vector;
using std::cin;

int main(void) {
    vector<int> nums;
    while (true) {
        char c; cin.get(c);
        if (c == '\n') break;
        if (c == ' ') nums.push_back(0);
        else          nums.push_back(c - '0');
    }
    char c;
    while (true) {
        cin.get(c);
        if (c == '*' || c == '+') break;
        for (int i = 0; i < nums.size(); i++) {
            if (c != ' ')
                nums[i] = nums[i] * 10 + (c - '0');
            cin.get(c);
        }
    }
    char op = c;
    uint64_t total = 0;
    uint64_t acc = nums[0];
    cin.get(c);
    for (int i = 1; i < nums.size(); i++) {
        cin.get(c);
        if (c != ' ') {
            op = c;
            total += acc;
            acc = nums[++i];
            cin.get(c);
        } else if (op == '+') {
            acc += nums[i];
        } else {
            acc *= nums[i];
        }
    }
    uint64_t ret = total + acc;
    std::cout << ret << std::endl;
    return 0;
}