from cmath import exp
from os import PRIO_USER
import utils
from queue import PriorityQueue
# from priority_queue import PriorityQueue
from node import Node

class AStar:
    def __init__(self, name, heuristic):
        self.name = name
        self.visited = {}
        self.heuristic = heuristic

    def h(self, x, goal_state_map):
        return self.heuristic(x.state, goal_state_map)

    def g(self, x):
        return 1

    def replace_item(self, queue, node):
        for i in range(len(queue)):
            if queue[i].id == node.id:
                queue[i].cost = node.cost
                break
    
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
            visited_edges[node.id] = node.cost

            nodes.append({ "id": node.id, "parent": node.parent, "action": node.action, "state": utils.get_output_state(node.state)})
            if node.compare_states(goal_state):
                result = node.state
                break

            count_states += 1
            for expanded_edge in node.expand_edge():
                cost = expanded_edge.depth + self.h(expanded_edge, goal_state_map)
                expanded_edge.cost = cost

                if expanded_edge.id in visited_edges and cost < visited_edges.get(expanded_edge.id):
                    visited_edges[expanded_edge.id] = expanded_edge.cost
                    self.replace_item(queue.queue, expanded_edge)
                    continue

                if expanded_edge.id not in visited_edges:
                    visited_edges[expanded_edge.id] = expanded_edge.cost
                    queue.put(expanded_edge)


        return {"nodes": nodes, "count_states": count_states, "result": result}
