import settings
import copy
from movement import Movement
from position import Position

class Node:
    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __init__(self, state_map, depth):
        self.movement = Movement()
        self.id = self.generate_id(state_map)
        self.cost = 0
        self.action = ""
        self.parent = ""
        self.state_map = state_map
        self.depth = depth

    def generate_id(self, state_map):
        id = ""
        for key in state_map.items():
            id += str(key[0]) + str(key[1].x) + str(key[1].y)

        return id


    def get_tile_position_by_value(self, value):
        if value in self.state_map:
            return self.state_map[value]

        return Position(-1, -1)

    def get_tile_value_by_pos(self, pos):
        for value in self.state_map.items():
            value_pos = value[1]
            if value_pos.x == pos.x and value_pos.y == pos.y:
                return value[0]

        return -1

    def get_manhattan_distance_sum(self, goal_state_map):
        s = 0

        for key in self.state_map.keys():
            current_pos = self.state_map[key]
            goal_pos = goal_state_map[key]
            s += (abs(current_pos.x -goal_pos.x) + abs(current_pos.y - goal_pos.y))

        return s

    def get_empty_tile_position(self):
        return self.get_tile_position_by_value(0)

    def expand_edge(self):
        parents = []
        empty_tile_position = self.get_empty_tile_position()
        possible_movements = self.movement.get_all_possible_movements(empty_tile_position)

        for possible_movement in possible_movements:
            state_copy = copy.deepcopy(self.state_map)
            tile_value_to_move = self.get_tile_value_by_pos(possible_movement)
            state_copy[0] = possible_movement
            state_copy[tile_value_to_move] = empty_tile_position
            new_node = Node(state_copy, self.depth + 1)
            new_node.parent = self.id
            parents.append(new_node)

        return parents


    def compare_states(self, goal_state_map):
        for key in self.state_map.keys():
            if self.state_map[key].x != goal_state_map[key].x and self.state_map[key].y != goal_state_map[key].y:
                return 0

        return 1

