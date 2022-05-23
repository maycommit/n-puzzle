import settings
import time

class Puzzle:
    def __init__(self, search_algorithm):
        settings.init(3)
        self.search_algorithm = search_algorithm

    def solve(self, initial_state, goal_state):
        start_time = time.time()
        result = self.search_algorithm.solve(initial_state, goal_state)

        result["name"] =  self.search_algorithm.name
        result["execution_time"] = time.time() - start_time
        return result

