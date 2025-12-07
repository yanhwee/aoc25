from sys import stdin

def parse(s: str) -> list[list[int]]:
    lines = s.strip().splitlines()
    ixs = (
        [i for i, x in enumerate(line) if x != '.']
        for line in lines)
    return list(filter(bool, ixs))

def solve(diagram: list[list[int]]) -> int:
    beams = set(diagram[0])
    count = 0
    for splitters in diagram[1:]:
        for split in splitters:
            if split in beams:
                beams.remove(split)
                beams.add(split + 1)
                beams.add(split - 1)
                count += 1
    return count

if __name__ == '__main__':
    print(solve(parse(stdin.read())))
    
