def is_safe_report(report):
    # Convert the report string into a list of integers
    levels = list(map(int, report.split()))
    
    # Check if the levels are strictly increasing or decreasing
    increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
    
    return increasing or decreasing

def can_be_safe_with_removal(levels):
    # Iterate through each level and check if removing it makes the report safe
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_report(' '.join(map(str, modified_levels))):
            return True
    return False

def count_safe_reports_part1(data):
    reports = data.strip().split('\n')
    safe_count = 0
    
    # Iterate through each report and check if it is safe
    for report in reports:
        if is_safe_report(report):
            print(f"Safe report (Part 1): {report}")
            safe_count += 1
        else:
            print(f"Unsafe report (Part 1): {report}")
    
    return safe_count

def count_safe_reports_part2(data):
    reports = data.strip().split('\n')
    safe_count = 0
    
    # Iterate through each report and check if it is safe or can be made safe by removing one level
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_report(report):
            print(f"Safe report (Part 2): {report}")
            safe_count += 1
        elif can_be_safe_with_removal(levels):
            print(f"Report made safe by removal (Part 2): {report}")
            safe_count += 1
        else:
            print(f"Unsafe report (Part 2): {report}")
    
    return safe_count

if __name__ == "__main__":
    # Read input data from file
    with open('input.txt', 'r') as file:
        input_data = file.read()
    
    # Count safe reports for Part 1
    part1_safe_count = count_safe_reports_part1(input_data)
    # Count safe reports for Part 2
    part2_safe_count = count_safe_reports_part2(input_data)
    
    # Print results
    print(f"Part 1: {part1_safe_count} safe reports")
    print(f"Part 2: {part2_safe_count} safe reports")