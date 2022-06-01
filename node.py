import settings
import movement
from position import Position

class Node:
    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __init__(self, state, level, real_cost=0, cost=0, action="", parent=""):
        self.id = self.generate_id(state)
        self.state = state
        self.level = level
        self.real_cost = real_cost
        self.cost = cost
        self.action = action
        self.parent = parent

    def set_cost(self, new_cost):
        self.cost = new_cost

    def g(self):
        return self.real_cost

    def generate_id(self, state):
        id = ""
        for i in range(len(state)):
            for j in range(len(state[i])):
                id += str(state[i][j])

        return id


    def get_tile_position(self, state, value):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == value:
                    return Position(i, j)

        return Position(-1, -1)

    def get_empty_tile_position(self):
        return self.get_tile_position(self.state, 0)

    def copy_state(self):
        copy = []
        for i in range(len(self.state)):
            row = []
            for j in range(len(self.state[i])):
                row.append(self.state[i][j])

            copy.append(row)

        return copy

    def expand(self):
        parents = []
        empty_position = self.get_empty_tile_position()
        movements = movement.get_all_possible_movements(empty_position)

        for m in movements:
            ex, ey = empty_position.x, empty_position.y
            mx, my = m.position.x, m.position.y
            state_copy = self.copy_state()
            state_copy[mx][my], state_copy[ex][ey] = state_copy[ex][ey], state_copy[mx][my]
            new_node = Node(
                state_copy,
                self.level + 1,
                real_cost=self.real_cost + 1,
                parent=self.id,
                action=m.name
            )
            parents.append(new_node)

        return parents


    def compare_states(self, goal_state):
        for i in range(settings.N):
            for j in range (settings.N):
                if self.state[i][j] != goal_state[i][j]:
                    return 0

        return 1
