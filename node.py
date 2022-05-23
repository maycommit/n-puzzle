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
        for i in range(len(state)):
            for j in range(len(state[i])):
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

    def copy_state(self):
        copy = []
        for i in range(len(self.state)):
            row = []
            for j in range(len(self.state[i])):
                row.append(self.state[i][j])

            copy.append(row)

        return copy

    def get_all_possible_movements(self, empty_tile_position):
        down = Position("DOWN", empty_tile_position.x, empty_tile_position.y - 1)
        up = Position("UP", empty_tile_position.x, empty_tile_position.y + 1)
        left = Position("LEFT", empty_tile_position.x + 1, empty_tile_position.y)
        right = Position("RIGHT", empty_tile_position.x - 1, empty_tile_position.y)

        return [down, up, left, right]

    def expand_edge(self):
        parents = []
        empty_tile_position = self.get_empty_tile_position()
        possible_movements = self.get_all_possible_movements(empty_tile_position)

        for possible_movement in possible_movements:
            is_valid_row_movement = possible_movement.x >= 0 and possible_movement.x < settings.N
            is_valid_column_movement = possible_movement.y >= 0 and possible_movement.y < settings.N

            if is_valid_row_movement and is_valid_column_movement:
                state_copy = self.copy_state()
                aux = state_copy[possible_movement.x][possible_movement.y]
                state_copy[possible_movement.x][possible_movement.y] = state_copy[empty_tile_position.x][empty_tile_position.y]
                state_copy[empty_tile_position.x][empty_tile_position.y] = aux
                new_node = Node(state_copy, self.depth + 1)
                new_node.action = possible_movement.name
                new_node.parent = self.id
                parents.append(new_node)

        return parents


    def compare_states(self, goal_state):
        for i in range(settings.N):
            for j in range (settings.N):
                if self.state[i][j] != goal_state[i][j]:
                    return 0

        return 1
