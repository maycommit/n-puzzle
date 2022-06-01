import unittest
import settings
import heuristics
import utils
from node import Node
from astar import AStar

settings.init(3)

class TestAStar(unittest.TestCase):
    def test_f(self):
        alg = AStar("A* (MD)", heuristics.calculate_manhattan_distance_sum)
        initial_state = [[1,4,2],[6,5,8],[7,3,0]]
        goal_state = [[1,4,2],[6,5,8],[7,3,0]]
        goal_state_map = utils.get_map_by_state(goal_state)
        x = Node(initial_state, 0)
        new_cost = alg.f(x, goal_state_map)
        self.assertEqual(new_cost, 10)

if __name__ == "__main__":
    unittest.main()

