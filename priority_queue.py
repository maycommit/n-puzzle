class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, cost, node):
        self.queue.append((cost, node))

    def delete(self):
        if len(self.queue) <= 0:
            return None

        item = sorted(self.queue, key=lambda item: item[0])[0]
        del self.queue[0]
        return item

    def empty(self):
        return len(self.queue) == 0
