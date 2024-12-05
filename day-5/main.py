from collections import defaultdict, deque

def parse_input(input_text):
    # Split the input text into rules section and updates section
    rules_section, updates_section = input_text.strip().split('\n\n')
    # Parse the rules into a list of tuples
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.split('\n')]
    # Parse the updates into a list of lists
    updates = [list(map(int, line.split(','))) for line in updates_section.split('\n')]
    return rules, updates

def is_correctly_ordered(update, rules):
    # Create a map of page indices for the current update
    index_map = {page: i for i, page in enumerate(update)}
    # Check each rule to see if it is violated
    for x, y in rules:
        if x in index_map and y in index_map and index_map[x] > index_map[y]:
            print(f"Rule {x}|{y} violated in update {update}")
            return False
    return True

def find_middle_page(update):
    # Find the middle index of the update
    n = len(update)
    middle_page = update[n // 2]
    print(f"Middle page of update {update} is {middle_page}")
    return middle_page

def topological_sort(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_set = set(update)
    
    # Build the graph and in-degree count based on the rules
    for x, y in rules:
        if x in pages_set and y in pages_set:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    print(f"Graph: {dict(graph)}")
    print(f"In-degree: {dict(in_degree)}")
    
    # Initialize the queue with nodes having zero in-degree
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    # Perform topological sort
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    print(f"Sorted update: {sorted_update}")
    return sorted_update

def solve_part_one(input_text):
    # Parse the input to get rules and updates
    rules, updates = parse_input(input_text)
    # Filter updates that are correctly ordered
    correctly_ordered_updates = [update for update in updates if is_correctly_ordered(update, rules)]
    # Calculate the sum of middle pages of correctly ordered updates
    middle_pages_sum = sum(find_middle_page(update) for update in correctly_ordered_updates)
    return middle_pages_sum

def solve_part_two(input_text):
    # Parse the input to get rules and updates
    rules, updates = parse_input(input_text)
    # Filter updates that are incorrectly ordered
    incorrectly_ordered_updates = [update for update in updates if not is_correctly_ordered(update, rules)]
    # Correctly order the updates using topological sort
    corrected_updates = [topological_sort(update, rules) for update in incorrectly_ordered_updates]
    # Calculate the sum of middle pages of corrected updates
    middle_pages_sum = sum(find_middle_page(update) for update in corrected_updates)
    return middle_pages_sum

# Read the input from the file
with open('input.txt', 'r') as file:
    input_text = file.read()

# Solve Part One
print("Solving Part One...")
result_part_one = solve_part_one(input_text)
print(f"Part One: {result_part_one}")

# Solve Part Two
print("Solving Part Two...")
result_part_two = solve_part_two(input_text)
print(f"Part Two: {result_part_two}")