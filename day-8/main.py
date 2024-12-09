from collections import defaultdict

class ResonantCollinearity:
    def __init__(self, file_path):
        # Initialize instance variables
        self.ants = defaultdict(list)
        self.alll = set()
        self.allowed = set()
        # Parse the input file and process the map data
        self.map_data = self.parse_input(file_path)
        print("Parsed map data:", self.map_data)
        self.process_map_data()
        print("Ants positions:", self.ants)
        print("Allowed positions:", self.allowed)
        print("All positions:", self.alll)

    @staticmethod
    def parse_input(file_path):
        # Read the input file and return a list of stripped lines
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    def process_map_data(self):
        # Process each line and character in the map data
        for i, line in enumerate(self.map_data):
            for j, c in enumerate(line):
                # Add the position to the allowed set
                self.allowed.add(i + 1j * j)
                if c != '.':
                    # Add the position to the ants dictionary and all positions set
                    self.ants[c].append(i + 1j * j)
                    self.alll.add(i + 1j * j)

    def solve(self, part):
        ats = set()

        # Iterate over each antenna type and their positions
        for antens in self.ants.values():
            for z in antens:
                for z_ in antens:
                    if z == z_:
                        continue
                    # Calculate the next position in the sequence
                    k = z + 2 * (z_ - z)
                    while k in self.allowed:
                        ats.add(k)
                        k += z_ - z
                        if part == 1:
                            break
        if part == 1:
            return len(ats)
        result = len(ats | self.alll)
        return result

    def main(self):
        # Print the results for part 1 and part 2
        print(f"part 1: {self.solve(1)}")
        print(f"part 2: {self.solve(2)}")

# Example usage:
if __name__ == "__main__":
    rc = ResonantCollinearity('input.txt')
    rc.main()