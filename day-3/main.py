import re

def parse_input(input_text, part):
    # Regular expression to find valid mul instructions
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    # Regular expression to find do and don't instructions
    control_pattern = re.compile(r'\b(do|don\'t)\(\)')

    # Split the input text into tokens
    tokens = re.split(r'(\bdo\(\)|\bdon\'t\(\)|mul\(\d+,\d+\))', input_text)
    
    enabled = True
    total_sum = 0

    for token in tokens:
        if part == 2 and control_pattern.match(token):
            if token == 'do()':
                enabled = True
                print(f"do() found, enabling mul instructions")
            elif token == 'don\'t()':
                enabled = False
                print(f"don't() found, disabling mul instructions")
        elif mul_pattern.match(token):
            x, y = map(int, mul_pattern.match(token).groups())
            if part == 1 or (part == 2 and enabled):
                total_sum += x * y
                print(f"mul({x},{y}) found, current sum: {total_sum}")
            else:
                print(f"mul({x},{y}) found but ignored due to don't()")

    return total_sum

# Read the input file
with open('input.txt', 'r') as file:
    input_text = file.read()

# Calculate the result for part 1
print("Executing Part 1")
result_part1 = parse_input(input_text, part=1)
print(f"Part 1 result: {result_part1}")

# Calculate the result for part 2
print("\nExecuting Part 2")
result_part2 = parse_input(input_text, part=2)
print(f"Part 2 result: {result_part2}")