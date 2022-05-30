
import unittest
from node import Node
from priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_case_1(self):
        p_queue = PriorityQueue()

        p_queue.put(Node([[111]], 1, 3))
        p_queue.put(Node([[111]], 1, 0))
        p_queue.put(Node([[222]], 2, 5))
        p_queue.put(Node([[333]], 2, 1))
        p_queue.put(Node([[444]], 2, 4))
        p_queue.replace(Node([[222]], 2, 3))
        p_queue.put(Node([[555]], 2, 1))
        p_queue.put(Node([[555]], 2, 10))
        p_queue.put(Node([[555]], 2, 6))

        result = []
        while not p_queue.empty():
            node = p_queue.get()
            result.append(str(node.cost))

        self.assertEqual(" ".join(result), "0 1 1 3 3 4 6 10")

if __name__ == "__main__":
    unittest.main()

