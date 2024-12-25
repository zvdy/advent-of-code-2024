from dataclasses import dataclass

grid = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        grid.append(line.strip())
n = len(grid)
m = len(grid[0])

@dataclass(frozen=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i + other.i, self.j + other.j)
    def __sub__(self, other):
        return Pos(self.i - other.i, self.j - other.j)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.i, self.j) == (other.i, other.j)
    def __hash__(self):
        return hash((self.i, self.j))
    def __lt__(self, other):
        return (self.i, self.j) < (other.i, other.j)
    def is_inbounds(self):
        return 0 <= self.i < n and 0 <= self.j < m
    def get_nbrs(self):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            yield self + delta

def dfs(start):
    q = [start]
    plant_type = grid[start.i][start.j]
    region = {start}
    while q:
        current = q.pop()
        for nbr in current.get_nbrs():
            if not nbr.is_inbounds():
                continue
            if nbr not in region and grid[nbr.i][nbr.j] == plant_type:
                q.append(nbr)
                region.add(nbr)
    return region

def get_perimeter(s):
    result = 0
    for p in s:
        perim = (4 - len(set(p.get_nbrs()) & s))
        result += perim
    return result

def get_sides(s):
    perimeter_edges = set()
    for p in s:
        for nbr in p.get_nbrs():
            if nbr not in s:
                perimeter_edges.add((p, nbr))
    sides = 0
    for p1, p2 in perimeter_edges:
        # check if leftmost or topmost
        if p1.j == p2.j:
            if (p1 - Pos(0, 1), p2 - Pos(0, 1)) not in perimeter_edges:
                sides += 1
        else:
            if (p1 - Pos(1, 0), p2 - Pos(1, 0)) not in perimeter_edges:
                sides += 1
    return sides

total_price1, total_price2 = 0, 0
candidates = {Pos(i, j) for i in range(n) for j in range(m)}
while candidates:
    start = candidates.pop()
    region = dfs(start)
    candidates -= region
    # calculate pricing
    area = len(region)
    perimeter = get_perimeter(region)
    total_price1 += (area * perimeter)
    sides = get_sides(region)
    total_price2 += (area * sides)
# part 1
print(total_price1)
# part 2
print(total_price2)