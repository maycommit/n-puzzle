from puzzle import Puzzle

def output(initial_state, goal_state):
    puzzle = Puzzle()
    alg1 = puzzle.resolve_with_breadth_first_search(initial_state, goal_state)
    alg2 = puzzle.resolve_with_a_star(initial_state, goal_state)
    d = {
        "BFS": [alg1.get("states"), alg1.get("result")],
        "A*": [alg2.get("states"), alg2.get("result")]
    }
    print ("{:<15} {:<10} {:<10}".format('Algorithm','States','Result'))
    for k, v in d.items():
        states, result = v
        result = "FOUND" if result else "NOT FOUND"

        print("{:<15} {:<10} {:<10}".format(k, states, result))


def test_puzzle():
    case1 = [[[4, 5, 1],[2, 3, 6],[0, 8, 7]], [[7, 5, 1],[2, 8, 6],[3, 4, 0]]]
    case2 = [[[4, 5, 1],[2, 3, 6],[0, 8, 7]], [[1, 2, 3],[4, 5, 6],[7, 8, 0]]]
    case3 = [[[1, 2, 3],[4, 5, 6],[7, 8, 0]], [[0, 1, 2],[3, 4, 5],[6, 7, 8]]]
    case4 = [[[1, 2, 3],[8, 0, 4],[7, 6, 5]], [[1, 3, 4],[8, 6, 2],[7, 0, 5]]]
    cases = [case1, case2, case3, case4]

    for ncase in cases:
        print("=========================================")
        initial_state, goal_state = ncase
        output(initial_state, goal_state)
        print("=========================================")



if __name__ == "__main__":
    test_puzzle()
