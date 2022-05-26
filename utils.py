import os
from position import Position

def open_statefile(initial_state, goal_state):
    filename = './out/' + initial_state + goal_state + '/states'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    return open(filename, 'w')

def open_resultfile(initial_state, goal_state):
    filename = './out/' + initial_state + goal_state + '/results'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    return open(filename, 'w')

def output_result(algorithms, initial_state, goal_state):
    result_file = open_resultfile(initial_state, goal_state)
    state_file = open_statefile(initial_state, goal_state)
    result_file.write("{:<15} {:<10} {:<15} {:<10}\n".format('Algorithm','States','Execution Time', 'Result'))

    for alg in algorithms:
        res = alg.solve(make_2d_array(initial_state), make_2d_array(goal_state))
        result_file.write("{:<15} {:<10} {:<15} {:<10}\n".format(res.get("name"), res.get("count_states"), str(res.get("execution_time"))[:8], str(res.get("result"))))
        for state in res.get("states"):
            state_file.write(str(state) + "\n")

def array2d_to_string(arr):
    return ','.join(str(item) for innerlist in outerlist for item in arr)

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
