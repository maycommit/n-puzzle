import utils
import heuristics
from puzzle import Puzzle
from bfs import BFS
from astar import AStar


while True:
    try:
        algs = [
            Puzzle(BFS("BFS")),
            Puzzle(AStar("A* (WP)", heuristics.calculate_wrong_positions_sum)),
            Puzzle(AStar("A* (MD)", heuristics.calculate_manhattan_distance_sum)),
        ]
        inputcase = input().split()
        initial_state, goal_state = inputcase
        utils.output_result(algs, initial_state, goal_state)
        print("Finish outputs for input: " + initial_state + " " + goal_state)
    except EOFError:
        break
