import utils
from priority_queue import PriorityQueue
from node import Node

class AStar:
    def __init__(self, name, heuristic):
        self.name = name
        self.visited = {}
        self.heuristic = heuristic

    def h(self, x, goal_state_map):
        return self.heuristic(x.state, goal_state_map)

    def g(self, x):
        return x.depth

    def solve(self, initial_state, goal_state):
        goal_state_map = utils.get_map_by_state(goal_state)

        result = None
        count_states = 0
        nodes = []
        visited_edges = {}
        queue = PriorityQueue()
        queue.put(Node(initial_state, 0))

        while not queue.empty():
            node = queue.get()
            if node.id in visited_edges and node.cost >= visited_edges.get(node.id):
                continue

            if node.compare_states(goal_state):
                result = node.state
                break

            count_states += 1
            visited_edges[node.id] = node.cost
            nodes.append({ "id": node.id, "parent": node.parent, "action": node.action, "state": utils.get_output_state(node.state)})
            for expanded_edge in node.expand_edge():
                cost = self.g(expanded_edge) + self.h(expanded_edge, goal_state_map)
                expanded_edge.cost = cost

                if expanded_edge.id not in visited_edges:
                    queue.put(expanded_edge)
                elif expanded_edge.id in visited_edges and cost < visited_edges.get(expanded_edge.id):
                    visited_edges[expanded_edge.id] = cost
                    queue.replace(expanded_edge)

        return {"nodes": nodes, "count_states": count_states, "result": result}
