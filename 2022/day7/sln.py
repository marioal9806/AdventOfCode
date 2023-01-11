"""
It will be a tree data structure
Every node will be a directory, that contains a list of files
And the children for every node will in turn be other directories
deeper into the structure.
"""

class Node:
    self.parent = None
    self.children = []
    self.files = []

    @property
    def size(self):
        sum = 0
        # First, add the size for your current files
        for file in self.files:
            sum += file.size

        # Then add the size of your child directories
        for child in self.children:
            sum += child.size


class File:
    self.name = None
    self.size = 0

    def __init__(self, name, size):
        self.name = name
        self.size = size


if __name__ == "__main__":
    root = Node()  # Don't lose the ref to root
    curr_node = root  # Will be our pointer throughout the tree

    with open("example.txt", "r") as input_file:
        # Parse each command
        for line in input_file:
            # If it is a command
            if line.startswith("$"):
                pass