def load_maze(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def find_guard(maze):
    DIRECTIONS = {'^', '>', 'v', '<'}
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell in DIRECTIONS:
                guard_pos = (r, c)
                guard_dir = cell
                maze[r][c] = '.'  # Clear the starting position
                return guard_pos, guard_dir
    return None, None

def simulate_guard_movement(maze, guard_pos, guard_dir):
    DIRECTIONS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    TURN_RIGHT = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    rows, cols = len(maze), len(maze[0])
    visited_positions = set()
    visited_positions.add(guard_pos)
    
    while True:
        next_r, next_c = guard_pos[0] + DIRECTIONS[guard_dir][0], guard_pos[1] + DIRECTIONS[guard_dir][1]
        
        if not (0 <= next_r < rows and 0 <= next_c < cols):  # Guard leaves the mapped area
            break
        
        if maze[next_r][next_c] == '#':  # Obstacle ahead, turn right
            guard_dir = TURN_RIGHT[guard_dir]
        else:  # Move forward
            guard_pos = (next_r, next_c)
            visited_positions.add(guard_pos)
    
    return len(visited_positions)

def main():
    file_path = 'input.txt'
    maze = load_maze(file_path)
    guard_pos, guard_dir = find_guard(maze)
    if guard_pos and guard_dir:
        distinct_positions = simulate_guard_movement(maze, guard_pos, guard_dir)
        print(distinct_positions)
    else:
        print("Guard not found in the maze.")

if __name__ == "__main__":
    main()