from puzzle import Puzzle
import settings

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

def make_2d_array(inp):
    res = []
    row = []
    for n in range(len(inp)):
        if len(row) == 3:
            res.append(row)
            row = []

        row.append(int(inp[n]))

    if len(row) > 0:
        res.append(row)

    return res


while True:
    try:
        inputcase = input().split()

        print("=========================================")
        initial_state, goal_state = inputcase
        output(make_2d_array(initial_state), make_2d_array(goal_state))
        print("=========================================")
    except EOFError:
        break
