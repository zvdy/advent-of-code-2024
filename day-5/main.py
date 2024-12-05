from collections import defaultdict, deque

def parse_input(input_text):
    rules_section, updates_section = input_text.strip().split('\n\n')
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.split('\n')]
    updates = [list(map(int, line.split(','))) for line in updates_section.split('\n')]
    return rules, updates

def is_correctly_ordered(update, rules):
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map and index_map[x] > index_map[y]:
            return False
    return True

def find_middle_page(update):
    n = len(update)
    return update[n // 2]

def topological_sort(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_set = set(update)
    
    for x, y in rules:
        if x in pages_set and y in pages_set:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def solve_part_one(input_text):
    rules, updates = parse_input(input_text)
    correctly_ordered_updates = [update for update in updates if is_correctly_ordered(update, rules)]
    middle_pages_sum = sum(find_middle_page(update) for update in correctly_ordered_updates)
    return middle_pages_sum

def solve_part_two(input_text):
    rules, updates = parse_input(input_text)
    incorrectly_ordered_updates = [update for update in updates if not is_correctly_ordered(update, rules)]
    corrected_updates = [topological_sort(update, rules) for update in incorrectly_ordered_updates]
    middle_pages_sum = sum(find_middle_page(update) for update in corrected_updates)
    return middle_pages_sum

# Read the input from the file
with open('input.txt', 'r') as file:
    input_text = file.read()

# Solve Part One
result_part_one = solve_part_one(input_text)
print(f"Part One: {result_part_one}")

# Solve Part Two
result_part_two = solve_part_two(input_text)
print(f"Part Two: {result_part_two}")