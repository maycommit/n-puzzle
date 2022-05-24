def calculate_manhattan_distance_sum(current_state, goal_state_map):
    s = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            current_tile = current_state[i][j]
            pos = goal_state_map[current_tile]
            s += (abs(i - pos.x) + abs(j - pos.y))

    return s

def calculate_wrong_positions_sum(current_state, goal_state_map):
    s = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            current_tile = current_state[i][j]
            goal_tile = goal_state_map[current_tile]

            if i == goal_tile.x and j == goal_tile.y:
                continue

            s += 1

    return s - 1

