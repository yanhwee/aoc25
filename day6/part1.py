from sys import stdin

def parse(s: str) -> tuple[list[int], list[int], list[int], list[int], list[str]]:
    a, b, c, d, e = s.strip().splitlines()
    a = list(map(int, a.split()))
    b = list(map(int, b.split()))
    c = list(map(int, c.split()))
    d = list(map(int, d.split()))
    e = e.split()
    return a, b, c, d, e

def solve(l1, l2, l3, l4, l5):
    calc = lambda a, b, c, d, e: (
        a + b + c + d if e == '+' else
        a * b * c * d)
    return sum(map(calc, l1, l2, l3, l4, l5))

if __name__ == '__main__':
    a, b, c, d, e = parse(stdin.read())
    print(solve(a, b, c, d, e))