import settings
import time
from position import Position

class Puzzle:
    def __init__(self, search_algorithm):
        settings.init(3)
        self.search_algorithm = search_algorithm

    def solve(self, initial_state, goal_state):
        initial_state_map = self.make_state_map(initial_state)
        goal_state_map = self.make_state_map(goal_state)

        start_time = time.time()
        result = self.search_algorithm.solve(initial_state_map, goal_state_map)

        result["name"] =  self.search_algorithm.name
        result["execution_time"] = time.time() - start_time
        return result

    def make_state_map(self, state):
        m = {}
        for i in range(len(state)):
            for j in range(len(state[i])):
                m[state[i][j]] = Position(i, j)

        return m


