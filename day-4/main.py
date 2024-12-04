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

    # Function to check if the pattern matches at a specific center (row, col)
    def is_xmas_center(row, col):
        # Define the pattern offsets for X-MAS:
        # M S (top arm)
        #  A  (center)
        # M S (bottom arm)
        pattern_offsets = [
            [(-1, -1), (1, 1)],  # M S (top-left to bottom-right)
            [(-1, 1), (1, -1)]   # M S (top-right to bottom-left)
        ]
        
        for offsets in pattern_offsets:
            try:
                if (grid[row + offsets[0][0]][col + offsets[0][1]] == 'M' and
                    grid[row][col] == 'A' and
                    grid[row + offsets[1][0]][col + offsets[1][1]] == 'S' and
                    grid[row + offsets[0][0]][col - offsets[0][1]] == 'M' and
                    grid[row + offsets[1][0]][col - offsets[1][1]] == 'S'):
                    return True
            except IndexError:
                continue
        return False

    # Iterate over the grid and count valid X-MAS patterns
    for row in range(1, rows - 1):  # Avoid edges (no valid X-MAS can be centered there)
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