import heapq

class PriorityQueue:

    def __init__(self):
        self.size = 0
        self.queue = []

    def __str__(self):
        return " ".join([str(x.cost) for x in self.queue])

    def put(self, node):
        self.queue.append(node)
        self._shift_up(self.size)
        self.size += 1

    def replace(self, node):
        item = node
        for i in range(len(self.queue)):
            if self.queue[i].id == node.id:
                item = self.queue[i]
                self._remove(i)
                item.cost = node.cost
                break

        self.put(item)

    def _shift_up(self, index):
        parent = int((index - 1)/2)

        while index > 0 and self.queue[parent].cost >= self.queue[index].cost:
            self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
            index = parent
            parent = int((parent - 1)/2)

    def _remove(self, index):
        self.size -= 1
        del self.queue[index]
        self._shift_down(index)


    def get(self):
        if self.size <= 0:
            raise Exception('The queue is empty')

        item = self.queue[0]
        self._remove(0)
        return item

    def _shift_down(self, parent):
        index = 2 * parent + 1
        while index < self.size:
            if index < self.size - 1:
                if self.queue[index].cost > self.queue[index + 1].cost:
                    index += 1

            if self.queue[parent].cost <= self.queue[index].cost:
                break

            self.queue[parent], self.queue[index] = self.queue[index], self.queue[parent]
            parent = index
            index = 2 * parent + 1

    def empty(self):
        return self.size == 0
