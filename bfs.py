from collections import deque
from node import Node

class BFS:
    def __init__(self):
        self.name = "BFS"
        self.visited = {}

    def solve(self, initial_state_map, goal_state_map):
        result = None
        count_states = 0
        visitedEdges = set()
        queue = deque([Node(initial_state_map, 0)])

        while queue:
            node = queue.popleft()
            visitedEdges.add(node.id)

            if node.compare_states(goal_state_map):
                result = node.state_map
                break

            count_states += 1
            for expanded_edge in node.expand_edge():
                if expanded_edge.id not in visitedEdges:
                    queue.append(expanded_edge)
                    visitedEdges.add(expanded_edge.id)

        return {"states": count_states, "result": result}

