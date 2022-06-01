import unittest
import movement
import settings
from position import Position

settings.init(3)

class TestMovement(unittest.TestCase):
    def test_get_two_possible_movements(self):
        empty_tile_position = Position(0, 0)
        possible_movements = movement.get_all_possible_movements(empty_tile_position)
        self.assertEqual(len(possible_movements), 2)
        self.assertEqual(possible_movements[0].name, 'LEFT')
        self.assertEqual(possible_movements[0].position.x, 0)
        self.assertEqual(possible_movements[0].position.y, 1)
        self.assertEqual(possible_movements[1].name, 'UP')
        self.assertEqual(possible_movements[1].position.x, 1)
        self.assertEqual(possible_movements[1].position.y, 0)

    def test_get_three_possible_movements(self):
        empty_tile_position = Position(1, 0)
        possible_movements = movement.get_all_possible_movements(empty_tile_position)
        self.assertEqual(len(possible_movements), 3)
        self.assertEqual(possible_movements[0].name, 'LEFT')
        self.assertEqual(possible_movements[0].position.x, 1)
        self.assertEqual(possible_movements[0].position.y, 1)
        self.assertEqual(possible_movements[1].name, 'UP')
        self.assertEqual(possible_movements[1].position.x, 2)
        self.assertEqual(possible_movements[1].position.y, 0)
        self.assertEqual(possible_movements[2].name, 'DOWN')
        self.assertEqual(possible_movements[2].position.x, 0)
        self.assertEqual(possible_movements[2].position.y, 0)


    def test_get_all_possible_movements(self):
        empty_tile_position = Position(1, 1)
        possible_movements = movement.get_all_possible_movements(empty_tile_position)
        self.assertEqual(len(possible_movements), 4)
        self.assertEqual(possible_movements[0].name, 'RIGHT')
        self.assertEqual(possible_movements[0].position.x, 1)
        self.assertEqual(possible_movements[0].position.y, 0)
        self.assertEqual(possible_movements[1].name, 'LEFT')
        self.assertEqual(possible_movements[1].position.x, 1)
        self.assertEqual(possible_movements[1].position.y, 2)
        self.assertEqual(possible_movements[2].name, 'UP')
        self.assertEqual(possible_movements[2].position.x, 2)
        self.assertEqual(possible_movements[2].position.y, 1)
        self.assertEqual(possible_movements[3].name, 'DOWN')
        self.assertEqual(possible_movements[3].position.x, 0)
        self.assertEqual(possible_movements[3].position.y, 1)

if __name__ == "__main__":
    unittest.main()

