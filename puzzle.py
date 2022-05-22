import copy
import settings
from collections import deque
from node import Node
from queue import PriorityQueue
from position import Position

class Puzzle:
    def __init__(self):
        settings.init(3)

    def get_all_possible_movements(self, empty_tile_position):
        down = Position("DOWN", empty_tile_position.x, empty_tile_position.y - 1)
        up = Position("UP", empty_tile_position.x, empty_tile_position.y + 1)
        left = Position("LEFT", empty_tile_position.x + 1, empty_tile_position.y)
        right = Position("RIGHT", empty_tile_position.x - 1, empty_tile_position.y)

        return [down, up, left, right]

    def h(self, x, goal_state):
        flat_curr_state = [item for sublist in x.state for item in sublist]
        flat_goal_state = [item for sublist in goal_state for item in sublist]
        return sum(abs(v1 - v2) for v1, v2 in zip(flat_curr_state, flat_goal_state))

    def g(self, x):
        return x.depth + 1

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
                new_node.action = possible_movement.name
                new_node.parent = edge.id
                parents.append(new_node)

        return parents

    def resolve_with_breadth_first_search(self, initial_state, goal_state):
        result = None
        count_states = 0
        visitedEdges = set()
        queue = deque([Node(initial_state, 0)])

        while queue:
            node = queue.popleft()
            visitedEdges.add(node.id)

            if node.compare_states(goal_state):
                result = node.state
                break

            count_states += 1
            for expanded_edge in self.expand_edge(node):
                if expanded_edge.id not in visitedEdges:
                    queue.append(expanded_edge)
                    visitedEdges.add(expanded_edge.id)

        return {"states": count_states, "result": result}

    def resolve_with_a_star(self, initial_state, goal_state):
        result = None
        count_states = 0
        visited_edges = {}
        queue = PriorityQueue()
        queue.put((0, Node(initial_state, 0)))

        while not queue.empty():
            queue_cost, node = queue.get()
            visited_edges[node.id] = queue_cost

            if node.compare_states(goal_state):
                result = node.state
                break

            count_states += 1
            for expanded_edge in self.expand_edge(node):
                expanded_edge.cost = self.g(expanded_edge) + self.h(expanded_edge, goal_state)
                visited_edge = visited_edges.get(expanded_edge.id)

                if visited_edge is None or visited_edge > expanded_edge.cost:
                    queue.put((expanded_edge.cost, expanded_edge))
                    visited_edges[expanded_edge.id] = expanded_edge.cost

        return {"states": count_states, "result": result}







