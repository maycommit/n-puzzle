from position import Position

def output(algorithms, initial_state, goal_state):
    d = {}
    for alg in algorithms:
        res = alg.solve(initial_state, goal_state)
        d[res.get("name")] = [res.get("states"), res.get("result"), res.get("execution_time")]

    print ("{:<15} {:<10} {:<15} {:<10}".format('Algorithm','States','Execution Time', 'Result'))
    for k, v in d.items():
        states, result, execution_time = v
        result = "FOUND" if result else "NOT FOUND"

        print("{:<15} {:<10} {:<15} {:<10}".format(k, states, str(execution_time)[:8], result))


def get_map_by_state(state):
    m = {}
    for i in range(len(state)):
        for j in range(len(state)):
            m[state[i][j]] = Position(i, j)

    return m


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
