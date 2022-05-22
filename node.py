import settings
from position import Position

class Node:
    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __init__(self, state, depth):
        self.id = self.generate_id(state)
        self.cost = 0
        self.action = ""
        self.parent = ""
        self.state = state
        self.depth = depth

    def generate_id(self, state):
        id = ""
        for i in range(settings.N):
            for j in range (settings.N):
                id += str(state[i][j])

        return id


    def get_empty_tile_position(self):
        for i in range(settings.N):
            for j in range (settings.N):
                if self.state[i][j] == 0:
                    return Position("", i, j)

        return Position("", 0, 0)

    def copy_state(self, puzzle_size):
        copy = []
        for i in range(puzzle_size):
            row = []
            for j in range (puzzle_size):
                row.append(self.state[i][j])

            copy.append(row)

        return copy

    def compare_states(self, goal_state):
        for i in range(settings.N):
            for j in range (settings.N):
                if self.state[i][j] != goal_state[i][j]:
                    return 0

        return 1
