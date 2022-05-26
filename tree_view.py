from collections import deque

class Node:
    def __init__(self, id, state):
        self.id = id
        self.state = []
        self.children = []

class TreeView:
    def __init__(self):
        self.root = None

    def add_node(self, parent, id, state):
        if self.root == None:
            self.root = Node(id, state)
            return

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            if node.id == parent:
                node.children.append(Node(id, state))
                return node

            for child in node.children:
                queue.append(child)




