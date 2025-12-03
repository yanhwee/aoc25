from sys import stdin
from typing import List

def parse(input: str) -> List[str]:
    return input.splitlines()

def solve(lines: List[str]) -> int:
    count = 0
    dial = 50
    for line in lines:
        op, n = line[0], int(line[1:])
        if op == 'L': dial = (100 - dial) % 100
        m, dial = divmod(dial + n, 100)
        count += m
        if op == 'L': dial = (100 - dial) % 100
    return count

if __name__ == "__main__":
    print(solve(parse(stdin.read())))