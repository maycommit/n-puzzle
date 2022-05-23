from queue import PriorityQueue
from node import Node

class AStar:
    def __init__(self):
        self.name = "A* (Man)"
        self.visited = {}

    def h(self, x, goal_state):
        return x.get_manhattan_distance_sum(goal_state)

    def g(self):
        return 1

    def solve(self, initial_state, goal_state):
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
            for expanded_edge in node.expand_edge():
                expanded_edge.cost = self.g() + self.h(expanded_edge, goal_state)
                visited_edge = visited_edges.get(expanded_edge.id)

                if visited_edge is None or visited_edge > expanded_edge.cost:
                    queue.put((expanded_edge.cost, expanded_edge))
                    visited_edges[expanded_edge.id] = expanded_edge.cost

        return {"states": count_states, "result": result}
