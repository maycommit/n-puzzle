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


    def get_tile_position(self, state, value):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == value:
                    return Position("", i, j)

        return Position("", -1, -1)


    def get_manhattan_distance_sum(self, goal_state):
        s = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                current_tile = self.state[i][j]
                pos = self.get_tile_position(goal_state, current_tile)
                s += (abs(i - pos.x) + abs(j - pos.y))
        return s

    def get_empty_tile_position(self):
        return self.get_tile_position(self.state, 0)

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
