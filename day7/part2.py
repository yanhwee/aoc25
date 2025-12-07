from sys import stdin
from functools import cache

def parse(s: str) -> list[list[int]]:
    lines = s.strip().splitlines()
    ixs = (
        [i for i, x in enumerate(line) if x != '.']
        for line in lines)
    return list(filter(bool, ixs))

def solve(diagram: list[list[int]]) -> int:
    sources, *diagram = diagram
    diagram = list(map(set, diagram))
    @cache
    def helper(i: int, j: int) -> int:
        if j >= len(diagram):
            return 1
        if i not in diagram[j]:
            return helper(i, j + 1)
        a = helper(i - 1, j + 1)
        b = helper(i + 1, j + 1)
        return a + b
    return sum(helper(s, 0) for s in sources)

if __name__ == '__main__':
    print(solve(parse(stdin.read())))
    
