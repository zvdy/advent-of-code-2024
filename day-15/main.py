from dataclasses import dataclass

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

grid = []
moves = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if line.startswith('#'):
            row = list(line.strip())
            if '@' in row:
                j = row.index('@')
                robot_pos = Pos(i, j)
                row[j] = '.'
            grid.append(row)
        else:
            moves.append(line.strip())
moves = ''.join(moves)
n = len(grid)
m = len(grid[0])

dirs = {'^': Pos(-1, 0), '>': Pos(0, 1), 'v': Pos(1, 0), '<': Pos(0, -1)}

for char in moves:
    dest = robot_pos + dirs[char]
    if grid[dest.i][dest.j] == '.':
        robot_pos = dest
    elif grid[dest.i][dest.j] == 'O':
        temp = dest
        while grid[temp.i][temp.j] == 'O':
            temp += dirs[char]
        if grid[temp.i][temp.j] == '.':
            grid[dest.i][dest.j] = '.'
            grid[temp.i][temp.j] = 'O'
            robot_pos = dest

gps = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'O':
            gps += (100*i + j)
print(gps)

# part 2
grid = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if line.startswith('#'):
            row = list(line.strip().replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.'))
            if '@' in row:
                j = row.index('@')
                robot_pos = Pos(i, j)
                row[j] = '.'
            grid.append(row)
n = len(grid)
m = len(grid[0])

for char in moves:
    dest = robot_pos + dirs[char]
    if grid[dest.i][dest.j] == '.':
        robot_pos = dest
    elif grid[dest.i][dest.j] in '[]':
        # find all box positions getting pushed
        q = [dest]
        boxes = {dest}
        while q:
            current = q.pop()
            nbrs = []
            if grid[current.i][current.j] == '[':
                nbrs.append(current + Pos(0, 1))
            else:
                nbrs.append(current + Pos(0, -1))
            nbrs.append(current + dirs[char])
            for nbr in nbrs:
                if nbr in boxes:
                    continue
                if grid[nbr.i][nbr.j] in '[]':
                    q.append(nbr)
                    boxes.add(nbr)
        # find all spaces in front of boxes getting pushed
        spaces = set()
        for box in boxes:
            space_ahead = box + dirs[char]
            if space_ahead not in boxes:
                spaces.add(space_ahead)
                if grid[space_ahead.i][space_ahead.j] == '#':
                    break
        # check if empty spaces in front, and apply push if so
        if all(grid[space.i][space.j] == '.' for space in spaces):
            def push_distance(box):
                if char in '<>':
                    return abs(box.j - dest.j)
                else:
                    return abs(box.i - dest.i)
            for box in sorted(boxes, key=push_distance, reverse=True):
                space_ahead = box + dirs[char]
                grid[box.i][box.j], grid[space_ahead.i][space_ahead.j] = grid[space_ahead.i][space_ahead.j], grid[box.i][box.j]
            robot_pos = dest

gps = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '[':
            gps += (100*i + j)
print(gps)