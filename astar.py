import utils
from priority_queue import PriorityQueue
from node import Node

class AStar:
    def __init__(self, name, heuristic):
        self.name = name
        self.visited_edges = {}
        self.opened_edges = PriorityQueue()
        self.heuristic = heuristic


    def h(self, x, goal_state_map):
        return self.heuristic(x.state, goal_state_map)

    def f(self, x, goal_state_map):
        return x.g() + self.h(x, goal_state_map)

    def _is_not_elegible(self, x):
        return x.id in self.visited_edges and x.cost >= self.visited_edges.get(x.id)

    def solve(self, initial_state, goal_state):
        goal_state_map = utils.get_map_by_state(goal_state)

        result = None
        count_states = 0
        nodes = []
        root_node = Node(initial_state, 0)
        self.opened_edges.put(root_node)

        while not self.opened_edges.empty():
            node = self.opened_edges.get()

            if node.compare_states(goal_state):
                result = node.state
                break

            count_states += 1
            nodes.append({ "id": node.id, "parent": node.parent, "action": node.action, "state": utils.get_output_state(node.state)})
            self.visited_edges[node.id] = node.cost
            for expanded_edge in node.expand_edge():
                new_cost = self.f(expanded_edge, goal_state_map)
                expanded_edge.set_cost(new_cost)

                if expanded_edge.id not in self.visited_edges:
                    self.opened_edges.put(expanded_edge)
                elif new_cost < self.visited_edges.get(expanded_edge.id):
                    self.opened_edges.replace_priority(expanded_edge)

        return {"nodes": nodes, "count_states": count_states, "result": result}
