import unittest
import heuristics
import utils

class TestHeuristics(unittest.TestCase):
    def test_manhattan_distance_case_1(self):
        test_state = [[7,2,4],[5,0,6],[8,3,1]]
        goal_state = utils.get_map_by_state([[0,1,2],[3,4,5],[6,7,8]])
        s = heuristics.calculate_manhattan_distance_sum(test_state, goal_state)
        self.assertEqual(s, 18)

    def test_manhattan_distance_case_2(self):
        test_state = [[8,1,3],[4,0,2],[7,6,5]]
        goal_state = utils.get_map_by_state([[1,2,3],[4,5,6],[7,8,0]])
        s = heuristics.calculate_manhattan_distance_sum(test_state, goal_state)
        self.assertEqual(s, 10)


    def test_wrong_poisition_case_1(self):
        test_state = [[7,2,4],[5,0,6],[8,3,1]]
        goal_state = utils.get_map_by_state([[0,1,2],[3,4,5],[6,7,8]])
        s = heuristics.calculate_wrong_positions_sum(test_state, goal_state)
        self.assertEqual(s, 8)

    def test_wrong_poisition_case_2(self):
        test_state = [[8,1,3],[4,0,2],[7,6,5]]
        goal_state = utils.get_map_by_state([[1,2,3],[4,5,6],[7,8,0]])
        s = heuristics.calculate_wrong_positions_sum(test_state, goal_state)
        self.assertEqual(s, 5)

if __name__ == "__main__":
    unittest.main()

