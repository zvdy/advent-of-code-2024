from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i + other.i, self.j + other.j)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.i, self.j) == (other.i, other.j)
    def __hash__(self):
        return hash((self.i, self.j))
    def get_nbrs(self):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            yield self + delta

@dataclass(frozen=True)
class Grid:
    grid: tuple[str]
    def height(self):
        return len(self.grid)
    def width(self):
        return len(self.grid[0])
    def __str__(self):
        return '\n'.join(self.grid)
    def get(self, pos: Pos):
        if self.is_inbounds(pos):
            return self.grid[pos.i][pos.j]
        return None
    def is_inbounds(self, pos):
        return 0 <= pos.i < self.height() and 0 <= pos.j < self.width()
    def bfs(self, start):
        q = deque()
        q.append(start)
        dist = {start: 0}
        while q:
            current = q.popleft()
            for nbr in current.get_nbrs():
                if self.get(nbr) == '#':
                    continue
                if nbr in dist:
                    continue
                dist[nbr] = dist[current] + 1
                q.append(nbr)
        return dist

grid = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        row = line.strip()
        if 'S' in row:
            j = row.find('S')
            start = Pos(i, j)
            row = row.replace('S', '.')
        if 'E' in row:
            j = row.find('E')
            end = Pos(i, j)
            row = row.replace('E', '.')
        grid.append(row)
grid = Grid(tuple(grid))

from_start = grid.bfs(start)
from_end = grid.bfs(end)
shortest_path = from_start[end]

def get_num_good_cheats(max_cheat_length, threshold):
    good_cheats = 0
    for i in range(grid.height()):
        for j in range(grid.width()):
            cheat_start = Pos(i, j)
            if grid.get(cheat_start) == '#':
                continue
            for ik in range(-max_cheat_length, max_cheat_length+1):
                jk_max = max_cheat_length - abs(ik)
                for jk in range(-jk_max, jk_max+1):
                    cheat_end = cheat_start + Pos(ik, jk)
                    if grid.is_inbounds(cheat_end) and grid.get(cheat_end) == '.':
                        path_length = from_start[cheat_start] + abs(ik) + abs(jk) + from_end[cheat_end]
                        if shortest_path - path_length >= threshold:
                            good_cheats += 1
    return good_cheats

# part 1
print(get_num_good_cheats(2, 100))

# part 2
print(get_num_good_cheats(20, 100))