from dataclasses import dataclass
from functools import cache
from itertools import permutations

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

codes = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        codes.append(line.strip())

# pad stuff
numpad = {'7': Pos(0, 0), '8': Pos(0, 1), '9': Pos(0, 2),
          '4': Pos(1, 0), '5': Pos(1, 1), '6': Pos(1, 2),
          '1': Pos(2, 0), '2': Pos(2, 1), '3': Pos(2, 2),
          '0': Pos(3, 1), 'A': Pos(3, 2)}
numpad_inv = {v: k for k,v in numpad.items()}
dirpad = {'^': Pos(0, 1), 'A': Pos(0, 2),
          '<': Pos(1, 0), 'v': Pos(1, 1), '>': Pos(1, 2)}
dirpad_inv = {v: k for k,v in dirpad.items()}
dirs = {'^': Pos(-1, 0), 'v': Pos(1, 0), '<': Pos(0, -1), '>': Pos(0, 1)}

@cache
def func(robot_id, current_key, dest_key, total_robots):
    pad, pad_inv = (numpad, numpad_inv) if robot_id == 0 else (dirpad, dirpad_inv)
    current_pos = pad[current_key]
    dest_pos = pad[dest_key]
    delta = dest_pos - current_pos
    if robot_id == total_robots-1:
        return abs(delta.i) + abs(delta.j) + 1
    seq = []
    for _ in range(abs(delta.i)):
        seq.append('^' if delta.i < 0 else 'v')
    for _ in range(abs(delta.j)):
        seq.append('<' if delta.j < 0 else '>')
    candidates = []
    if not seq:
        return 1
    for r in set(permutations(seq)):
        pos = current_pos
        steps = 0
        for i, dir_key in enumerate(r):
            steps += func(robot_id+1, 'A' if i == 0 else r[i-1], dir_key, total_robots)
            pos += dirs[dir_key]
            if pos not in pad_inv:
                break
        else:
            steps += func(robot_id + 1, r[-1], 'A', total_robots)
            candidates.append(steps)
    return min(candidates)

# part 1 and 2
total_complexity = 0
for num_robots in [3, 26]:
    for code in codes:
        complexity = func(0, 'A', code[0], num_robots)
        for i in range(1, len(code)):
            complexity += func(0, code[i-1], code[i], num_robots)
        total_complexity += complexity * int(code[:-1])
    print(total_complexity)