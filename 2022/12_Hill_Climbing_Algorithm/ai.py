from collections import deque
import sys



def solve(grid, start, end):
    # Initialize the queue with the starting position
    queue = deque([start])
    # Keep track of the number of steps taken to reach each position
    steps = {start: 0}

    # Perform the search
    while queue:
        #input()
        curr_pos = queue.popleft()
        print(f"curr_pos={curr_pos} {grid[curr_pos[1]][curr_pos[0]]}  steps={steps[curr_pos]}")
        if curr_pos == end:
            return steps[curr_pos]

        # Consider all valid moves from the current position
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
            if not is_valid_move(grid, curr_pos, next_pos, steps):
                continue
            queue.append(next_pos)
            steps[next_pos] = steps[curr_pos] + 1
    return -1  # Destination not reached

def is_valid_move(grid, curr_pos, next_pos, steps):
    # Check if the move is out of bounds
    if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
        return False

    # Check if the destination square has already been visited
    if next_pos in steps:
        return False

    # Check if the destination square has an elevation that is at most one higher than the current position
    curr_elevation = ord(grid[curr_pos[1]][curr_pos[0]]) - ord('a')
    next_elevation = ord(grid[next_pos[1]][next_pos[0]]) - ord('a')
    if next_elevation > curr_elevation + 1:
        return False

    return True

with open(sys.argv[1], mode='r') as infile:
     grid = infile.read().strip().split('\n')

solve(grid,(0,20),(55,20))
