def load_word_search(file_path):
    """Load the word search grid from a file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def count_xmas_occurrences(grid):
    """Count the number of XMAS occurrences in the word search grid."""
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, down-right, down-left
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, up-left, up-right
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search_from(x, y, dx, dy):
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search_from(i, j, dx, dy):
                    count += 1
    return count

def count_xmas_patterns(grid):
    """Count the number of X-MAS patterns in the word search grid."""
    rows = len(grid)
    cols = len(grid[0])
    xmas_count = 0

    # Helper function to check MAS sequences
    def is_mas_sequence(c1, c2, c3):
        return (c1, c2, c3) in [("M", "A", "S"), ("S", "A", "M")]

    # Function to validate the X-MAS pattern centered at (row, col)
    def is_xmas_center(row, col):
        try:
            # Extract potential arms
            top_left = (grid[row - 1][col - 1], grid[row][col], grid[row + 1][col + 1])
            top_right = (grid[row - 1][col + 1], grid[row][col], grid[row + 1][col - 1])

            # Check if both are valid MAS sequences
            return is_mas_sequence(*top_left) and is_mas_sequence(*top_right)
        except IndexError:
            return False  # Out of bounds

    # Iterate over all potential centers in the grid
    for row in range(1, rows - 1):  # Avoid edges
        for col in range(1, cols - 1):  # Avoid edges
            if is_xmas_center(row, col):
                xmas_count += 1

    return xmas_count

if __name__ == "__main__":
    # Load the word search grid from input.txt
    grid = load_word_search("input.txt")
    
    # Part 1: Count the number of XMAS occurrences
    xmas_occurrences = count_xmas_occurrences(grid)
    print("Number of XMAS occurrences:", xmas_occurrences)
    
    # Part 2: Count the number of X-MAS patterns
    xmas_patterns = count_xmas_patterns(grid)
    print("Number of X-MAS patterns:", xmas_patterns)