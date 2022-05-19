from puzzle import Puzzle

def test_puzzle_1():
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
    assert puzzle.state_count == 2

def test_puzzle_2():
    initial_state = [
        [4, 5, 1],
        [2, 3, 6],
        [0, 8, 7],
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]

    puzzle = Puzzle()
    puzzle.resolve_with_breadth_first_search(initial_state, goal_state)
    assert puzzle.state_count == 181440

if __name__ == "__main__":
    test_puzzle_1()
    test_puzzle_2()
    print("Everything passed")
