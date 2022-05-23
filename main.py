from puzzle import Puzzle
from bfs import BFS
from a_star import AStar

def output(initial_state, goal_state):
    algs = [
        Puzzle(BFS()),
        Puzzle(AStar())
    ]

    d = {}
    for alg in algs:
        res = alg.solve(initial_state, goal_state)
        d[res.get("name")] = [res.get("states"), res.get("result"), res.get("execution_time")]

    print ("{:<15} {:<10} {:<15} {:<10}".format('Algorithm','States','Execution Time', 'Result'))
    for k, v in d.items():
        states, result, execution_time = v
        result = "FOUND" if result else "NOT FOUND"

        print("{:<15} {:<10} {:<15} {:<10}".format(k, states, str(execution_time)[:8], result))

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
