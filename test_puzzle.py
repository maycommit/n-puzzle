from puzzle import Puzzle

def test_puzzle():
    initial_state = [
        [4, 5, 1],
        [2, 3, 6],
        [0, 8, 7],
    ]

    goal_state = [
        [4, 5, 1],
        [0, 3, 6],
        [2, 8, 7],
    ]

    puzzle = Puzzle()
    puzzle.resolve_with_breadth_first_search(initial_state, goal_state)
    print(puzzle.state_count)
    assert puzzle.state_count == 2

if __name__ == "__main__":
    test_puzzle()
