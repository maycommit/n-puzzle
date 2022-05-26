import utils
import heuristics
from puzzle import Puzzle
from bfs import BFS
from a_star import AStar

algs = [
    Puzzle(BFS("BFS")),
    Puzzle(AStar("A* (WP)", heuristics.calculate_wrong_positions_sum)),
    Puzzle(AStar("A* (MD)", heuristics.calculate_manhattan_distance_sum)),
]

while True:
    try:
        inputcase = input().split()
        initial_state, goal_state = inputcase
        utils.output_result(algs, initial_state, goal_state)
        print("Finish outputs for input: " + initial_state + " " + goal_state)
    except EOFError:
        break
