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

    def has_lower_cost(self, node):
        return node.cost < self.visited_edges.get(node.id)


    def solve(self, initial_state, goal_state):
        goal_state_map = utils.get_map_by_state(goal_state)
        nodes, count_states, result = [], 0, None

        root_node = Node(initial_state, 0, real_cost=0)
        self.opened_edges.put(root_node)

        while not self.opened_edges.empty():
            edge = self.opened_edges.get()
            if edge.id in self.visited_edges and not self.has_lower_cost(edge):
                continue

            if edge.state == goal_state:
                result = edge.state
                break

            count_states += 1
            nodes.append({ "id": edge.id, "parent": edge.parent, "action": edge.action, "state": utils.get_output_state(edge.state)})
            self.visited_edges[edge.id] = edge.cost
            for expanded_edge in edge.expand():
                new_cost = self.f(expanded_edge, goal_state_map)
                expanded_edge.set_cost(new_cost)

                if expanded_edge.id not in self.visited_edges:
                    self.opened_edges.put(expanded_edge)
                elif expanded_edge.id in self.visited_edges and self.has_lower_cost(expanded_edge):
                    self.opened_edges.replace_priority(expanded_edge)
                    self.visited_edges[expanded_edge.id] = expanded_edge.cost

        return {"nodes": nodes, "count_states": count_states, "result": result}
