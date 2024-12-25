from dataclasses import dataclass
import re
from itertools import count


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

robots = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        pattern = r'p=(.+),(.+) v=(.+),(.+)'
        px, py, vx, vy = (int(z) for z in re.match(pattern, line).groups())
        robots.append((Pos(px, py), Pos(vx, vy)))

n, m = 103, 101

def get_dest(pos, vel, steps):
    x = (pos.x + vel.x * steps) % m
    y = (pos.y + vel.y * steps) % n
    return Pos(x, y)

steps = 100
tl, tr, bl, br = 0, 0, 0, 0
for p, v in robots:
    dest = get_dest(p, v, steps)
    if dest.x < m//2:
        if dest.y < n//2:
            tl += 1
        elif dest.y > n//2:
            bl += 1
    elif dest.x > m//2:
        if dest.y < n//2:
            tr += 1
        elif dest.y > n//2:
            br += 1
print(tl*tr*bl*br)

def contains_cluster(l):
    largest_group = 0
    candidates = set(l)
    num = len(candidates)
    while candidates:
        q = [list(candidates)[0]]
        visited = {q[0]}
        while q:
            current = q.pop()
            for nbr in current.get_nbrs():
                if nbr in candidates and nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        largest_group = max(largest_group, len(visited))
        candidates -= visited
    return largest_group >= num // 4

# part 2
robot_pos = [robot[0] for robot in robots]
for seconds in count(1):
    for i in range(len(robot_pos)):
        x = (robot_pos[i].x + robots[i][1].x) % m
        y = (robot_pos[i].y + robots[i][1].y) % n
        robot_pos[i] = Pos(x, y)
    s = set(robot_pos)
    if contains_cluster(robot_pos):
        print('Seconds:', seconds)
        for y in range(n):
            row = ''.join('#' if Pos(x, y) in s else '.' for x in range(m))
            print(row)
        break
