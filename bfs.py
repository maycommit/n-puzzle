import utils
from collections import deque
from node import Node

class BFS:
    def __init__(self, name):
        self.name = name
        self.visited = {}

    def solve(self, initial_state, goal_state):
        result = None
        count_states = 0
        nodes = []
        visitedEdges = set()
        queue = deque([Node(initial_state, 0)])

        while queue:
            node = queue.popleft()
            if node.id in visitedEdges:
                continue

            nodes.append({ "id": node.id, "parent": node.parent, "action": node.action, "state": utils.get_output_state(node.state)})
            if node.compare_states(goal_state):
                result = node.state
                break

            count_states += 1
            visitedEdges.add(node.id)
            for expanded_edge in node.expand():
                if expanded_edge.id not in visitedEdges:
                    queue.append(expanded_edge)

        return {"nodes": nodes, "count_states": count_states, "result": result}

