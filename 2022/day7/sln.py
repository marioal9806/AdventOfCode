"""
It will be a tree data structure
Every node will be a directory, that contains a list of files
And the children for every node will in turn be other directories
deeper into the structure.
"""

from typing import List

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.size} {self.name}"


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children: List[Node] = []
        self.files: List[File] = []

    @property
    def size(self) -> int:
        sum = 0
        # First, add the size for your current files
        for file in self.files:
            sum += file.size

        # Then add the size of your child directories
        for child in self.children:
            sum += child.size

        return sum

    def find_child_by_name(self, name) -> File:
        for child in self.children:
            if child.name == name:
                return child


if __name__ == "__main__":
    root = Node("/")  # Don't lose the ref to root
    curr_node = root  # Will be our pointer throughout the tree

    with open("example.txt", "r") as input_file:
        # Parse each command
        for line in input_file:
            if line.startswith("$"): # It is a command
                [cmd, *args] = line.lstrip("$").split(" ")  # Parse command
                match cmd:
                    case "ls":
                        pass  # The listing of files & directories comes next
                    case "cd":
                        if args[0] == "..":  # Move to your parent
                            curr_node = curr_node.parent
                        else:  # Move to one of your children
                            curr_node = curr_node.find_child_by_name(args[0])
                    case _:  # We only have two commands, throw error
                        raise ValueError(f"Command not supported: {cmd}")
            else:  # We're parsing files and directories
                pass  # TODO: Parse files
                # Save them into the current node
