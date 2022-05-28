import os
import json
import shutil
from position import Position

def open_nodefile(initial_state, goal_state):
    filename = './out/' + initial_state + goal_state + '/nodes.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    return open(filename, 'w')

def open_resultfile(initial_state, goal_state):
    filename = './out/' + initial_state + goal_state + '/results.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    return open(filename, 'w')

def copy_viewer(initial_state, goal_state):
    shutil.copy('viewer/index.html', "out/{0}{1}/index.html".format(initial_state, goal_state))

def output_result(algorithms, initial_state, goal_state):
    result_file = open_resultfile(initial_state, goal_state)
    node_file = open_nodefile(initial_state, goal_state)
    node_lines = []
    result_lines = []

    for alg in algorithms:
        res = alg.solve(make_2d_array(initial_state), make_2d_array(goal_state))
        result_lines.append({"name": res.get("name"), "count_states": res.get("count_states"), "execution_time": str(res.get("execution_time"))[:8], "result": str(res.get("result"))})
        node_lines.append({ "algorithm": res.get("name"), "nodes": res.get("nodes") })

    node_file.write(json.dumps(node_lines))
    result_file.write(json.dumps(result_lines))
    copy_viewer(initial_state, goal_state)


def get_output_state(state):
    res = ""
    for i in range(len(state)):
        res += ' {} | {} | {}'.format(*state[i])
        if i < len(state) - 1:
            res += '\n--+--+--\n'

    return res
        

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
