from collections import Counter

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)

    return total_distance

def calculate_similarity_score(left_list, right_list):
    # Count the occurrences of each number in the right list
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_count[num]

    return similarity_score

def read_input_file(file_path):
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

# Read the input file
left_list, right_list = read_input_file('input.txt')

# Calculate the total distance
total_distance = calculate_total_distance(left_list, right_list)
print(f"Total distance: {total_distance}")

# Calculate the similarity score
similarity_score = calculate_similarity_score(left_list, right_list)
print(f"Similarity score: {similarity_score}")