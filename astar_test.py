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
        goal_state = [[1,2,0],[3,4,5],[6,7,8]]
        goal_state_map = utils.get_map_by_state(goal_state)
        x = Node(initial_state, 2, real_cost=2)
        new_cost = alg.f(x, goal_state_map)
        self.assertEqual(new_cost, 10)

    def test_h(self):
        alg1 = AStar("A* (WP)", heuristics.calculate_wrong_positions_sum)
        alg2 = AStar("A* (MD)", heuristics.calculate_manhattan_distance_sum)
        initial_state = [[1,4,2],[6,5,8],[7,3,0]]
        goal_state = [[1,2,0],[3,4,5],[6,7,8]]
        goal_state_map = utils.get_map_by_state(goal_state)
        x = Node(initial_state, 2, real_cost=2)
        h1_res = alg1.h(x, goal_state_map)
        h2_res = alg2.h(x, goal_state_map)
        self.assertEqual(h1_res, 7)
        self.assertEqual(h2_res, 8)

if __name__ == "__main__":
    unittest.main()

