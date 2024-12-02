def is_safe_report(report):
    levels = list(map(int, report.split()))
    increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def can_be_safe_with_removal(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_report(' '.join(map(str, modified_levels))):
            return True
    return False

def count_safe_reports_part1(data):
    reports = data.strip().split('\n')
    safe_count = sum(1 for report in reports if is_safe_report(report))
    return safe_count

def count_safe_reports_part2(data):
    reports = data.strip().split('\n')
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_report(report) or can_be_safe_with_removal(levels):
            safe_count += 1
    return safe_count

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input_data = file.read()
    
    part1_safe_count = count_safe_reports_part1(input_data)
    part2_safe_count = count_safe_reports_part2(input_data)
    
    print(f"Part 1: {part1_safe_count} safe reports")
    print(f"Part 2: {part2_safe_count} safe reports")