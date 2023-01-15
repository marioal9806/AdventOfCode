import unittest
from sln import File, Node


class TestFile(unittest.TestCase):
    def setUp(self):
        self.file = File("a", 200)

    def test_init(self):
        self.assertEqual(self.file.size, 200, "Should be 200")
        self.assertEqual(self.file.name, "a", "Should be a")

    def test_str(self):
        self.assertEqual(str(self.file), "200 a")


class TestNode(unittest.TestCase):
    """
    Create a Node, add 2 files and a child with its own file
    """

    def setUp(self):
        self.node = Node("/")

    def test_size_w_files(self):
        self.node.files.extend([File("a", 200), File("b", 400)])
        self.assertEqual(self.node.size, 600, "Should be 600")

    def test_size_w_child_dir(self):
        child_node = Node("c", self.node)
        child_node.files.extend([File("a", 200), File("b", 400)])
        self.node.children.append(child_node)
        self.node.files.append(File("c", 100))
        self.assertEqual(self.node.size, 700, "Should be 700")

    def test_find_child_by_name(self):
        node_to_find = Node("b", self.node)
        self.node.children.extend(
            [
                Node("a", self.node),
                node_to_find,
                Node("c", self.node)
            ]
        )
        self.assertIs(self.node.find_child_by_name("b"), node_to_find)


if __name__ == "__main__":
    unittest.main()
