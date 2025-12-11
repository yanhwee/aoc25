from sys import stdin
from functools import cache

def parse(s: str) -> list[tuple[str, list[str]]]:
    def parse_line(s: str) -> tuple[str, list[str]]:
        a, b = s.split(': ')
        return a, b.split(' ')
    return list(map(parse_line, s.strip().splitlines()))

def solve(edges: list[tuple[str, list[str]]]):
    edges = dict(edges)
    
    @cache
    def count_paths(node) -> int:
        if node == 'out':
            return 1
        return sum(map(count_paths, edges[node]))
    
    return count_paths('you')

if __name__ == '__main__':
    print(solve(parse(stdin.read())))