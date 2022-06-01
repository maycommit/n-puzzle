import unittest
import settings
from node import Node

settings.init(3)

class TestNote(unittest.TestCase):
    def test_generate_id(self):
        state = [[1,2,3],[4,5,6],[7,8,0]]
        node = Node(state, 0)
        id = node.generate_id(state)
        self.assertEqual(id, "123456780")

    def test_get_tile_position(self):
        state = [[1,2,3],[4,5,6],[7,8,0]]
        node = Node(state, 0)
        tile_position = node.get_tile_position(state, 4)
        self.assertEqual([tile_position.x, tile_position.y], [1, 0])

    def test_get_tile_position_failed(self):
        state = [[1,2,3],[4,5,6],[7,8,0]]
        node = Node(state, 0)
        tile_position = node.get_tile_position(state, 9)
        self.assertEqual([tile_position.x, tile_position.y], [-1, -1])

    def test_get_empty_tile_position(self):
        state = [[1,2,3],[4,5,6],[7,8,0]]
        node = Node(state, 0)
        tile_position = node.get_empty_tile_position()
        self.assertEqual([tile_position.x, tile_position.y], [2, 2])

    def test_copy_paste(self):
        state = [[1,2,3],[4,5,6],[7,8,0]]
        node = Node(state, 0)
        original = node.state
        cstate = node.copy_state()
        original[0][0] = 1
        self.assertEqual(state, cstate)

    def test_expand_edge(self):
        state = [[7,2,4],[5,0,6],[8,3,1]]
        node = Node(state, 0)
        expand_edges = node.expand()
        self.assertEqual(expand_edges[0].state, [[7,2,4],[0,5,6],[8,3,1]])
        self.assertEqual(expand_edges[0].parent, '724506831')
        self.assertEqual(expand_edges[0].real_cost, 1)
        self.assertEqual(expand_edges[0].action, 'RIGHT')
        self.assertEqual(expand_edges[1].state, [[7,2,4],[5,6,0],[8,3,1]])
        self.assertEqual(expand_edges[1].parent, '724506831')
        self.assertEqual(expand_edges[1].real_cost, 1)
        self.assertEqual(expand_edges[1].action, 'LEFT')
        self.assertEqual(expand_edges[2].state, [[7,2,4],[5,3,6],[8,0,1]])
        self.assertEqual(expand_edges[2].parent, '724506831')
        self.assertEqual(expand_edges[2].real_cost, 1)
        self.assertEqual(expand_edges[2].action, 'UP')
        self.assertEqual(expand_edges[3].state, [[7,0,4],[5,2,6],[8,3,1]])
        self.assertEqual(expand_edges[3].parent, '724506831')
        self.assertEqual(expand_edges[3].real_cost, 1)
        self.assertEqual(expand_edges[3].action, 'DOWN')

    def test_compare_states(self):
        state = [[7,2,4],[5,0,6],[8,3,1]]
        node = Node(state, 0)
        self.assertEqual(node.compare_states(state), 1)

    def test_compare_states_failed(self):
        state = [[7,2,4],[5,0,6],[8,3,1]]
        goal = [[7,2,4],[5,6,0],[8,3,1]]
        node = Node(state, 0)
        self.assertEqual(node.compare_states(goal), 0)

if __name__ == "__main__":
    unittest.main()

