import settings
from position import Position

class Movement:
    def __init__(self) -> None:
        pass

    def get_all_possible_movements(self, tile_position):
        possible_movements = []
        all_movements = [
            Position(tile_position.x, tile_position.y - 1),
            Position(tile_position.x, tile_position.y + 1),
            Position(tile_position.x + 1, tile_position.y),
            Position(tile_position.x - 1, tile_position.y),
        ]

        for movement in all_movements:
            is_valid_row_movement = movement.x >= 0 and movement.x < settings.N
            is_valid_column_movement = movement.y >= 0 and movement.y < settings.N

            if is_valid_row_movement and is_valid_column_movement:
                possible_movements.append(movement)

        return possible_movements


