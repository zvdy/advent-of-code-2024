from itertools import product

class BridgeRepair:

    def __init__(self):
        self.calibrations = []
        self.invalid_in_part1 = []
        # Read and parse the input file
        with open('input.txt', 'r') as f:
            for line in f.readlines():
                temp = line.split(': ')
                temp[0] = int(temp[0])
                temp[1] = [int(x) for x in temp[1].split(' ')]
                self.calibrations.append(temp)
        self.part1 = 0
        self.part2 = 0

    def place_operators(self, part: str):
        # Define the set of operators to use based on the part
        ops = [0, 1] if part == 'part1' else [0, 1, 2]
        # Select the calibrations to process based on the part
        cals = self.calibrations if part == 'part1' else self.invalid_in_part1
        for cal in cals:
            found = False
            # Try all possible combinations of operators
            for choice in product(ops, repeat=len(cal[1])-1):
                # Check if the current combination of operators achieves the goal
                if cal[0] == self.use_choice(cal[1], choice, cal[0]):
                    # Update the results for part1 and part2
                    self.part1 += cal[0] if part == 'part1' else 0
                    self.part2 += cal[0]
                    found = True
                    break
            # If no valid combination is found in part1, add to invalid list
            if not found and part == 'part1':
                self.invalid_in_part1.append(cal)

    def use_choice(self, cal_list: list[int], choice: int, goal: int):
        # Apply the chosen operators to the calibration list
        temp = cal_list[0]
        for i, val in enumerate(choice):
            if val == 0:
                temp += cal_list[i + 1]
            elif val == 1:
                temp *= cal_list[i + 1]
            else:
                temp = int(str(temp) + str(cal_list[i + 1]))
            # Stop if the temporary result exceeds the goal
            if temp > goal:
                break
        return temp

if __name__ == '__main__':
    # Create an instance of BridgeRepair and solve for both parts
    day7 = BridgeRepair()
    day7.place_operators('part1')
    day7.place_operators('part2')
    # Print the results for part1 and part2
    print(day7.part1, day7.part2)