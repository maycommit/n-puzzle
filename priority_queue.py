import bisect

class PriorityQueue:

    def __init__(self):
        self.size = 0
        self.queue = []
        self.entries = set()

    def __str__(self):
        return " ".join([str(x.cost) for x in self.queue])

    def heapify(self, index):
        left = 2 * index
        right = (2 * index) + 1
        size = len(self.queue)
        minn = index

        if left < size and self.queue[left].cost < self.queue[index].cost:
            minn = left

        if right < size and self.queue[right].cost < self.queue[minn].cost:
            minn = right

        if minn != index:
            self.queue[index], self.queue[minn] = self.queue[minn], self.queue[index]
            self.heapify(minn)

    def put(self, node):
        index = len(self.queue)
        for i in range(len(self.queue)):
          if self.queue[i].cost > node.cost:
            index = i
            break

        if index == len(self.queue):
          self.queue = self.queue[:index] + [node]
        else:
          self.queue = self.queue[:index] + [node] + self.queue[index:]


    def _shift_down(self, index):
        while index > 0 and self.queue[self._parent(index)].cost >= self.queue[index].cost:
            self.queue[index], self.queue[self._parent(index)] = self.queue[self._parent(index)], self.queue[index]
            index = self._parent(index)


    def _parent(self, index):
        return index // 2

    def replace_priority(self, node):
        for i in range(len(self.queue)):
            if self.queue[i].id == node.id:
                print('REPLACE')

    def get(self):
        return self.queue.pop(0)


    def empty(self):
        return len(self.queue) == 0
