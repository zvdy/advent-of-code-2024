import argparse
from itertools import batched

class DiskFragmenter:
    def __init__(self, layout):
        self.layout = layout

    def read_input(self, filename):
        # Read the input file and convert the first line to a list of integers
        with open(filename, 'r') as file:
            line = file.readline().strip()
            return list(map(int, line))

    def get_memory(self):
        memory = []
        is_file = True
        file_id = 0
        for s in self.layout:
            if is_file:
                # Add file_id repeated s times to memory
                memory.extend([int(file_id)] * s)
                file_id += 1
            else:
                # Add None repeated s times to memory
                memory.extend([None] * s)

            # Alternate between file and free space
            is_file = not is_file
        return memory

    def part1(self, memory):
        left = 0
        right = len(memory) - 1

        # Walk inwards from each side while
        # swapping "not None" from the right with "None" on the left
        while left < right:
            while memory[left] is not None:
                left += 1
            while memory[right] is None:
                right -= 1
            while (left < right
                   and memory[left] is None
                   and memory[right] is not None):
                # Swap elements
                memory[left], memory[right] = memory[right], memory[left]
                left += 1
                right -= 1

        # Calculate checksum
        s = 0
        for i, m in enumerate(memory):
            if m is None:
                continue
            s += i * m
        return s

    def part2(self):
        data_blocks = []
        free_blocks = []
        file_id = 0
        # Create parallel lists representing chunks
        # of data, and the free space following it
        for b in batched(self.layout, 2):
            data_size, *rest = b
            empty_size = rest[0] if len(rest) == 1 else 0

            # Append data blocks and free blocks
            data_blocks.append([file_id] * data_size)
            free_blocks.append([[], empty_size])
            file_id += 1

        # Defragment
        candidate_id = len(data_blocks)
        while candidate_id > 1:
            candidate_id -= 1
            candidate_data = data_blocks[candidate_id]
            candidate_len = len(candidate_data)

            # Find a free block with enough space for current candidate
            for i in range(candidate_id):
                # Skip if this free block is too small to hold the candidate data
                if free_blocks[i][1] < candidate_len:
                    continue

                # Move candidate data into the free block, and update its size
                free_blocks[i][0].extend(candidate_data)
                free_blocks[i][1] -= candidate_len

                # Null the original data block
                data_blocks[candidate_id] = [None] * candidate_len
                break

        # Calculate checksum
        s, pos = 0, 0
        for i in range(len(data_blocks)):
            for d in data_blocks[i]:
                s += (d or 0) * pos
                pos += 1
            for d in free_blocks[i][0]:
                s += d * pos
                pos += 1
            pos += free_blocks[i][1]

        return s


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser("main.py")
    parser.add_argument("filename", nargs='?',
                        help="input filename", default="input.txt")
    args = parser.parse_args()

    # Read layout from input file
    fragmenter = DiskFragmenter([])
    layout = fragmenter.read_input(args.filename)
    fragmenter.layout = layout

    # Calculate and print checksum for part 1
    checksum = fragmenter.part1(fragmenter.get_memory())
    print(f"\nPart1: checksum = {checksum}")

    # Calculate and print checksum for part 2
    checksum = fragmenter.part2()
    print(f"Part2: checksum = {checksum}\n")