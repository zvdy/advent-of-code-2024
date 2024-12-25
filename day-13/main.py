import re
from z3.z3 import *
from dataclasses import dataclass


@dataclass(frozen=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i + other.i, self.j + other.j)
    def scalar_mul(self, a):
        return Pos(a*self.i, a*self.j)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.i, self.j) == (other.i, other.j)
    def __hash__(self):
        return hash((self.i, self.j))

def get_min_tokens(a_vector, b_vector, prize_vector):
    l = Int('l')
    m = Int('m')
    s = Optimize()
    s.add(l >= 0)
    s.add(m >= 0)
    s.add(l * a_vector.i + m * b_vector.i == prize_vector.i)
    s.add(l * a_vector.j + m * b_vector.j == prize_vector.j)
    h = s.minimize(3*l + m)
    s.check()
    s.lower(h)
    result = s.model()
    if result[l] is not None:
        return 3*result[l].as_long() + result[m].as_long()
    else:
        return None

min_tokens1, min_tokens2 = 0, 0
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if i%4 == 0:
            pattern = r'Button A: X\+(\d+), Y\+(\d+)'
            ax, ay = (int(z) for z in re.match(pattern, line).groups())
        elif i%4 == 1:
            pattern = r'Button B: X\+(\d+), Y\+(\d+)'
            bx, by = (int(z) for z in re.match(pattern, line).groups())
        elif i%4 == 2:
            pattern = r'Prize: X=(\d+), Y=(\d+)'
            px, py = (int(z) for z in re.match(pattern, line).groups())
            # part 1
            tokens = get_min_tokens(Pos(ax, ay), Pos(bx, by), Pos(px, py))
            if tokens is not None:
                min_tokens1 += tokens
            # part 2
            px, py = 10000000000000 + px, 10000000000000 + py
            tokens = get_min_tokens(Pos(ax, ay), Pos(bx, by), Pos(px, py))
            if tokens is not None:
                min_tokens2 += tokens

# part 1
print(min_tokens1)
# part 2
print(min_tokens2)