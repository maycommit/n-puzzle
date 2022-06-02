import unittest
from node import Node
from priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_case_1(self):
        p_queue = PriorityQueue()

        p_queue.put(Node([[000]], 1, cost=3))
        p_queue.put(Node([[111]], 1, cost=0))
        p_queue.put(Node([[222]], 2, cost=5))
        p_queue.put(Node([[333]], 2, cost=1))
        p_queue.put(Node([[444]], 2, cost=4))
        p_queue.replace_priority(Node([[222]], 2, cost=3))
        p_queue.put(Node([[555]], 2, cost=2))
        p_queue.put(Node([[666]], 2, cost=10))
        p_queue.put(Node([[777]], 2, cost=6))

        result = []
        while not p_queue.empty():
            node = p_queue.get()
            result.append(str(node.cost))

        self.assertEqual(" ".join(result), "0 1 2 3 3 4 6 10")

if __name__ == "__main__":
    unittest.main()

