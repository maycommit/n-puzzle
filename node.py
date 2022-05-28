import settings
import movement
from position import Position

class Node:
    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __init__(self, state, depth, cost=0, action="", parent=""):
        self.id = self.generate_id(state)
        self.cost = cost
        self.action = action
        self.parent = parent
        self.state = state
        self.depth = depth

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

    def expand_edge(self):
        parents = []
        empty_position = self.get_empty_tile_position()
        movements = movement.get_all_possible_movements(empty_position)

        for m in movements:
            state_copy = self.copy_state()
            aux = state_copy[m.position.x][m.position.y]
            state_copy[m.position.x][m.position.y] = state_copy[empty_position.x][empty_position.y]
            state_copy[empty_position.x][empty_position.y] = aux
            new_node = Node(state_copy, self.depth + 1, parent=self.id, action=m.name)
            parents.append(new_node)

        return parents


    def compare_states(self, goal_state):
        for i in range(settings.N):
            for j in range (settings.N):
                if self.state[i][j] != goal_state[i][j]:
                    return 0

        return 1
