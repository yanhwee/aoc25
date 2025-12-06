from sys import stdin
from operator import add, mul

def parse(s: str) -> list[str]:
    return s.splitlines()

def solve(lines: list[str]) -> int:
    *lines, ops = lines
    total = 0
    acc = 0
    op = None
    for i in range(-1, len(ops)):
        if i + 1 < len(ops) and ops[i + 1] != ' ':
            total += acc
            op = add if ops[i + 1] == '+' else mul
            acc = 0 if ops[i + 1] == '+' else 1
            continue
        col = (l[i] for l in lines)
        num = 0
        for c in col:
            if c == ' ':
                continue
            c = int(c)
            num = num * 10 + c
        acc = op(acc, num)
    return total + acc

if __name__ == '__main__':
    print(solve(parse(stdin.read())))