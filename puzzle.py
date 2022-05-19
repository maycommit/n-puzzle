import copy
import settings
from collections import deque
from node import Node
from position import Position

class Puzzle:
    def __init__(self):
        settings.init(3)
        self.state_count = 0

    def get_all_possible_movements(self, empty_tile_position):
        down = Position(empty_tile_position.x, empty_tile_position.y - 1)
        up = Position(empty_tile_position.x, empty_tile_position.y + 1)
        left = Position(empty_tile_position.x + 1, empty_tile_position.y)
        right = Position(empty_tile_position.x - 1, empty_tile_position.y)

        return [down, up, left, right]


    def expand_edge(self, edge):
        parents = []
        empty_tile_position = edge.get_empty_tile_position()
        possible_movements = self.get_all_possible_movements(empty_tile_position)

        for possible_movement in possible_movements:
            is_valid_row_movement = possible_movement.x >= 0 and possible_movement.x < settings.N
            is_valid_column_movement = possible_movement.y >= 0 and possible_movement.y < settings.N

            if is_valid_row_movement and is_valid_column_movement:
                state_copy = copy.deepcopy(edge.state)
                aux = state_copy[possible_movement.x][possible_movement.y]
                state_copy[possible_movement.x][possible_movement.y] = state_copy[empty_tile_position.x][empty_tile_position.y]
                state_copy[empty_tile_position.x][empty_tile_position.y] = aux
                new_node = Node(state_copy, edge.depth + 1)
                parents.append(new_node)

        return parents


    def resolve_with_breadth_first_search(self, initial_state, goal_state):
        visitedEdges = set()
        queue = deque([Node(initial_state, 0)])

        while queue:
            node = queue.popleft()
            visitedEdges.add(node.id)

            if node.compare_states(goal_state):
                return node.state

            self.state_count += 1
            for expanded_edge in self.expand_edge(node):
                if expanded_edge.id not in visitedEdges:
                    queue.append(expanded_edge)
                    visitedEdges.add(expanded_edge.id)

        return





