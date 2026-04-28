import unittest
from tree import Tree


class TestFind(unittest.TestCase):

    def test_find_existing_value(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)

        result = tree._find(2, tree.root)

        self.assertIsNotNone(result)
        self.assertEqual(result.data, 2)

    def test_find_missing_value(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)

        result = tree._find(99, tree.root)

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
