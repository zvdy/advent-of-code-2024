from functools import cache

designs = []
with open('input.txt', 'r') as f:
    towels = f.readline().strip().split(', ')
    f.readline()
    for line in f.readlines():
        designs.append(line.strip())

@cache
def num_arrangements(design, start=0):
    if start >= len(design):
        return 1
    result = 0
    for towel in towels:
        if design[start: start+len(towel)] == towel:
            result += num_arrangements(design, start+len(towel))
    return result

# part 1
print(sum(num_arrangements(design) > 0 for design in designs))

# part 2
print(sum(map(num_arrangements, designs)))