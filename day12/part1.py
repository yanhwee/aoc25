from pprint import pprint
from sys import stdin

def parse(s: str) -> tuple[list[list[list[bool]]], list[tuple[tuple[int, int], list[int]]]]:
    *xs, ls = s.strip().split('\n\n')

    def parse_shape(s: str) -> list[list[bool]]:
        _, *xs = s.splitlines()
        return [[c == '#' for c in x] for x in xs]
    
    def parse_line(s: str) -> tuple[tuple[int, int], list[int]]:
        rc, xs = s.split(': ')
        r, c = rc.split('x')
        r, c = int(r), int(c)
        ys = list(map(int, xs.split(' ')))
        return (r, c), ys
    
    shapes = list(map(parse_shape, xs))
    lines = list(map(parse_line, ls.splitlines()))
    return shapes, lines

def solve(shapes: list[list[list[bool]]], boxes: list[tuple[tuple[int, int], list[int]]]):
    pass

if __name__ == '__main__':
    pprint(parse(stdin.read()))