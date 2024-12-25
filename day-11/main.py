from functools import cache

with open('input.txt', 'r') as f:
    stones = [int(x) for x in f.readline().split()]

@cache
def get_span(stone, num_blinks):
    if num_blinks == 0:
        return 1
    if stone == 0:
        return get_span(1, num_blinks-1)
    elif len(str(stone)) % 2 == 0:
        n = len(str(stone))
        left = int(str(stone)[:n // 2])
        right = int(str(stone)[n // 2:])
        return get_span(left, num_blinks-1) + get_span(right, num_blinks-1)
    else:
        return get_span(2024*stone, num_blinks-1)

# part 1
num = 25
print(sum(get_span(x, num) for x in stones))

# part 2
num = 75
print(sum(get_span(x, num) for x in stones))
