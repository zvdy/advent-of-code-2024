from collections import defaultdict

secrets = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        secrets.append(int(line))

def evolve(num):
    result = num
    result = ((result*64) ^ result) % 16777216
    result = ((result//32) ^ result) % 16777216
    result = ((result*2048) ^ result) % 16777216
    return result

price_lists = []
part_1_result = 0
for secret in secrets:
    num = secret
    price_lists.append([num%10])
    for _ in range(2000):
        num = evolve(num)
        price_lists[-1].append(num%10)
    part_1_result += num

# part 1
print(part_1_result)

# part 2
diff_table = defaultdict(int)
for p in price_lists:
    d = set()
    for i in range(4, len(p)):
        diff = (p[i-3] - p[i-4], p[i-2] - p[i-3], p[i-1] - p[i-2], p[i] - p[i-1])
        if diff in d:
            continue
        diff_table[diff] += p[i]
        d.add(diff)
print(max(diff_table.values()))