import time
import heapq
from queue import Queue
from collections import namedtuple

# Define the puzzle state
class PuzzleState:
    def __init__(self, puzzle, parent=None, move=""):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.cost = 0 if parent is None else parent.cost + 1

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return self.puzzle == other.puzzle if isinstance(other, PuzzleState) else False

    def __hash__(self):
        return hash(str(self.puzzle))

    def __repr__(self):
        return f"Move: {self.move}\n{self.puzzle[0]}\n{self.puzzle[1]}\n{self.puzzle[2]}\n"

    def heuristic(self):
        # A simple heuristic: count the number of misplaced tiles
        return sum([1 if self.puzzle[i][j] != (i * 3 + j + 1) % 9 else 0 for i in range(3) for j in range(3)])


def get_neighbors(state):
    neighbors = []
    i, j = next((i, j) for i in range(3) for j in range(3) if state.puzzle[i][j] == 0)

    def is_valid_move(x, y):
        return 0 <= x < 3 and 0 <= y < 3

    moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for x, y in moves:
        if is_valid_move(x, y):
            new_puzzle = [row[:] for row in state.puzzle]
            new_puzzle[i][j], new_puzzle[x][y] = new_puzzle[x][y], new_puzzle[i][j]
            neighbors.append(PuzzleState(new_puzzle, state, move=f"{state.puzzle[i][j]}->{state.puzzle[x][y]}"))

    return neighbors


def breadth_first_search(initial_state, goal_state):
    queue = Queue()
    visited = set()
    queue.put(initial_state)

    while not queue.empty():
        current_state = queue.get()
        if current_state.puzzle == goal_state.puzzle:
            return current_state
        visited.add(current_state)
        neighbors = get_neighbors(current_state)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.put(neighbor)

    return None


def a_star_search(initial_state, goal_state):
    heap = []
    heapq.heappush(heap, initial_state)
    visited = set()

    while heap:
        current_state = heapq.heappop(heap)
        if current_state.puzzle == goal_state.puzzle:
            return current_state
        visited.add(current_state)
        neighbors = get_neighbors(current_state)
        for neighbor in neighbors:
            if neighbor not in visited:
                heapq.heappush(heap, neighbor)

    return None


def depth_first_search(initial_state, goal_state):
    stack = [initial_state]
    visited = set()

    while stack:
        current_state = stack.pop()
        if current_state.puzzle == goal_state.puzzle:
            return current_state
        visited.add(current_state)
        neighbors = get_neighbors(current_state)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

    return None


def measure_algorithm(algorithm, initial_state, goal_state):
    start_time = time.time()
    solution = algorithm(initial_state, goal_state)
    end_time = time.time()
    time_taken = end_time - start_time

    return solution, time_taken


def print_solution(solution):
    path = []
    while solution:
        path.append(solution.move)
        solution = solution.parent
    for move in reversed(path):
        print(move)


if __name__ == "__main__":
    # Define initial and goal states
    initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    initial_state = PuzzleState(initial_state)
    goal_state = PuzzleState(goal_state)

    # Measure Breadth-First Search
    bfs_solution, bfs_time = measure_algorithm(breadth_first_search, initial_state, goal_state)

    # Measure A* Search
    astar_solution, astar_time = measure_algorithm(a_star_search, initial_state, goal_state)

    # Measure Depth-First Search
    dfs_solution, dfs_time = measure_algorithm(depth_first_search, initial_state, goal_state)

    # Print results
    print("Breadth-First Search:")
    if bfs_solution:
        print_solution(bfs_solution)
        print(f"Number of moves: {bfs_solution.cost}")
        print(f"Time taken: {bfs_time:.6f} seconds")
    else:
        print("No solution found.")

    print("\nA* Search:")
    if astar_solution:
        print_solution(astar_solution)
        print(f"Number of moves: {astar_solution.cost}")
        print(f"Time taken: {astar_time:.6f} seconds")
    else:
        print("No solution found.")

    print("\nDepth-First Search:")
    if dfs_solution:
        # print_solution(dfs_solution)
        print(f"Number of moves: {dfs_solution.cost}")
        print(f"Time taken: {dfs_time:.6f} seconds")
    else:
        print("No solution found.")
