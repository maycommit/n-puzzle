from collections import deque
from node import Node

class BFS:
    def __init__(self, name):
        self.name = name
        self.visited = {}

    def solve(self, initial_state, goal_state):
        result = None
        count_states = 0
        visitedEdges = set()
        queue = deque([Node(initial_state, 0)])

        while queue:
            node = queue.popleft()
            visitedEdges.add(node.id)

            if node.compare_states(goal_state):
                result = node.state
                print(node.action)
                break

            count_states += 1
            for expanded_edge in node.expand_edge():
                if expanded_edge.id not in visitedEdges:
                    queue.append(expanded_edge)
                    visitedEdges.add(expanded_edge.id)

        return {"states": count_states, "result": result}

