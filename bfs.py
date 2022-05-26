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
            visitedEdges.add(node.id)

            nodes.append({ "id": node.id, "parent": node.parent, "action": node.action, "state": str(node.state)})
            if node.compare_states(goal_state):
                result = node.state
                break

            count_states += 1
            for expanded_edge in node.expand_edge():
                if expanded_edge.id not in visitedEdges:
                    queue.append(expanded_edge)
                    visitedEdges.add(expanded_edge.id)

        return {"nodes": nodes, "count_states": count_states, "result": result}

