from dataclasses import dataclass
from collections import deque

n, m = 71, 71

@dataclass(frozen=True)
class Pos:
    x: int
    y: int
    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.x, self.y) == (other.x, other.y)
    def __hash__(self):
        return hash((self.x, self.y))
    def is_inbounds(self):
        return 0 <= self.x < m and 0 <= self.y < n
    def get_nbrs(self):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            if (self+delta).is_inbounds():
                yield self + delta

bytes = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split(','))
        bytes.append(Pos(x, y))

def bfs(start, goal, obstacles):
    q = deque()
    q.append(start)
    dist = {start: 0}
    while q:
        current = q.popleft()
        for nbr in current.get_nbrs():
            if nbr in obstacles:
                # print(current, nbr)
                continue
            if nbr in dist:
                continue
            dist[nbr] = dist[current] + 1
            if nbr == goal:
                return dist[nbr]
            q.append(nbr)

# part 1
obstacles = set(bytes[:1024])
print(bfs(Pos(0, 0), Pos(m-1, n-1), obstacles))

# part 2
for i in range(1024, len(bytes)):
    obstacles.add(bytes[i])
    if bfs(Pos(0, 0), Pos(m-1, n-1), obstacles) is None:
        break
print('{},{}'.format(bytes[i].x, bytes[i].y))