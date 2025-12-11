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
    def count_paths(node, fft, dac) -> int:
        if node == 'out':
            return 1 if fft and dac else 0
        if node == 'fft':
            fft = True
        elif node == 'dac':
            dac = True
        return sum(count_paths(n, fft, dac) for n in edges[node])
    
    return count_paths('svr', False, False)

if __name__ == '__main__':
    print(solve(parse(stdin.read())))