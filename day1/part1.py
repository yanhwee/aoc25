from sys import stdin
from typing import List

def parse(input: str) -> List[str]:
    return input.splitlines()

def solve(lines: List[str]) -> int:
    count = 0
    dial = 50
    for line in lines:
        op, n = line[0], int(line[1:])
        if op == 'L': n = -n
        dial += n
        dial %= 100
        if dial == 0:
            count += 1
    return count

if __name__ == "__main__":
    print(solve(parse(stdin.read())))