import settings
from position import Position

class Movement:
    def __init__(self, name, x, y):
        self.name = name
        self.position = Position(x, y)


def get_all_possible_movements(empty_tile_position):
    possible_movements = []
    down = Movement("LEFT", empty_tile_position.x, empty_tile_position.y - 1)
    up = Movement("RIGHT", empty_tile_position.x, empty_tile_position.y + 1)
    left = Movement("UP", empty_tile_position.x + 1, empty_tile_position.y)
    right = Movement("DOWN", empty_tile_position.x - 1, empty_tile_position.y)

    for movement in [down, up, left, right]:
        is_valid_row_movement = movement.position.x >= 0 and movement.position.x < settings.N
        is_valid_column_movement = movement.position.y >= 0 and movement.position.y < settings.N

        if is_valid_row_movement and is_valid_column_movement:
            possible_movements.append(movement)

    return possible_movements
