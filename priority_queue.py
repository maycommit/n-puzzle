class PriorityQueue:

    def __init__(self):
        self.size = 0
        self.queue = []
        self.entries = set()

    def __str__(self):
        return " ".join([str(x.cost) for x in self.queue])

    def heapify(self, index):
        left = 2 * index + 1
        right = (2 * index + 1) + 1
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
        self.queue.append(node)
        self._shift_down(0)

    def _shift_down(self, index):
        size = len(self.queue) - 1
        new_item = self.queue[size]

        while size > index:
            parent_index = (size - 1) >> 1
            parent = self.queue[parent_index]
            if new_item.cost <= parent.cost:
                self.queue[size] = parent
                size = parent_index
                continue
            break
        self.queue[size] = new_item

    def _parent(self, index):
        return (index - 1) // 2

    def replace_priority(self, node):
        replaced_item = None
        for i in range(len(self.queue)):
            if self.queue[i].id == node.id:
                replaced_item = self.queue[i]
                self.queue[i].cost = node.cost
                self._shift_down(i)
                break

        if not replaced_item:
            self.put(node)

    def get(self):
        last = self.queue.pop()
        if self.queue:
            item = self.queue[0]
            self.queue[0] = last
            self.heapify(0)
            return item

        return last


    def empty(self):
        return len(self.queue) == 0
