from sys import stdin
from math import dist
from itertools import combinations
from heapq import heapify, heappop

class UnionFind:
    def __init__(self, xs):
        self.parent = {x: x for x in xs}
        self.size = {x: 1 for x in xs}
    def find_root(self, p):
        parent = self.parent
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p
    def union(self, p, q):
        parent = self.parent
        size = self.size
        p = self.find_root(p)
        q = self.find_root(q)
        if (size[p] > size[q]):
            parent[q] = p
            size[p] += size[q]
        else:
            parent[p] = q
            size[q] += size[p]
    def find(self, p, q):
        return self.find_root(p) == self.find_root(q)

def parse(s: str) -> list[tuple[int, int, int]]:
    return [
        tuple(map(int, line.split(',')))
        for line in s.strip().splitlines()]

def solve(coords: list[tuple[int, int, int]]) -> int:
    pairs = combinations(coords, 2)
    pairs = [(dist(a, b), a, b) for a, b in pairs]
    heapify(pairs)
    uf = UnionFind(coords)
    for _ in range(len(coords) - 1):
        while True:
            _, a, b = heappop(pairs)
            if not uf.find(a, b):
                break
        uf.union(a, b)
    return a[0] * b[0]

if __name__ == '__main__':
    print(solve(parse(stdin.read())))