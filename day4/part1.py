from sys import stdin

def parse(s: str) -> list[list[str]]:
    return list(map(list, s.splitlines()))

def solve(grid: list[list[str]]):
    DIRS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]
    n = len(grid)
    m = len(grid[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '@': continue
            c = 0
            for (a, b) in DIRS:
                if not (0 <= i + a < n): continue
                if not (0 <= j + b < m): continue
                if grid[i + a][j + b] == '@':
                    c += 1
            if c < 4:
                count += 1
    return count

if __name__ == '__main__':
    print(solve(parse(stdin.read())))