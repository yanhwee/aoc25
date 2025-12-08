from sys import stdin
from math import dist, prod
from itertools import combinations
from heapq import heapify, heappop, nlargest

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
    k = 1000
    pairs = combinations(coords, 2)
    pairs = [(dist(a, b), a, b) for a, b in pairs]
    heapify(pairs)
    uf = UnionFind(coords)
    for _ in range(k):
        _, a, b = heappop(pairs)
        if uf.find(a, b):
            continue
        uf.union(a, b)
    roots = set(map(uf.find_root, coords))
    sizes = (uf.size[r] for r in roots)
    return prod(nlargest(3, sizes))

if __name__ == '__main__':
    print(solve(parse(stdin.read())))