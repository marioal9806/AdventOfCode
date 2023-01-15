"""
It will be a tree data structure
Every node will be a directory, that contains a list of files
And the children for every node will in turn be other directories
deeper into the structure.

Pt. 1:
Guessed 201_875, too low
Guessed 2_011_005, too high
Guessed 1_423_358 -> Right Answer!
"""

from typing import List


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.size} {self.name}"


class Node:
    target_children: List['Node'] = []
    target_sum: int = 0

    def __init__(self, name: str, parent: 'Node' = None):
        self.name = name
        self.parent: Node = parent
        self.children: List[Node] = []
        self.files: List[File] = []

    def __str__(self):
        return f"{self.name} {self.size}"

    @property
    def size(self) -> int:
        node_size: int = 0
        # Then add the size of your child directories
        for child in self.children:
            node_size += child.size

        # First, add the size for your current files
        for file in self.files:
            node_size += file.size

        if node_size <= 100_000:
            Node.target_sum += node_size

        return node_size

    def find_child_by_name(self, name: str) -> 'Node':
        for child in self.children:
            if child.name == name:
                return child

    def add_nodes_gt(self, target_size) -> None:
        for child in self.children:
            child.add_nodes_gt(target_size)
        if self.size >= target_size:
            Node.target_children.append(self)


def parse_commands(root: Node, commands) -> None:
    """
    Grabs a root node and any iterable of strings, where each line
    corresponds to a command or a file being listed.
    Fills the root node with the tree-like references to the
    directories and files within it.
    """
    next(input_file)  # Skip '/' insertion
    curr_node = root  # Will be our pointer throughout the tree
    for line in input_file:  # Parse each command
        if line.startswith("$"):  # It is a command
            [cmd, *args] = line.lstrip("$").strip().split(" ")  # Parse command
            match cmd:
                case "ls":
                    pass  # The listing of files & directories comes next
                case "cd":
                    if args[0] == "..":  # Move to your parent
                        curr_node = curr_node.parent
                    else:  # Move to one of your children
                        curr_node = curr_node.find_child_by_name(args[0])
                        if curr_node is None:  # Child does not exist
                            raise ValueError(f"Child {args[0]} not found")
                case _:  # We only have two commands, throw error
                    raise ValueError(f"Command not supported: {cmd}")
        else:  # We're parsing files and directories
            if line.startswith("dir"):  # If dir, save it as a child node
                [_, name] = line.strip().split(" ")
                curr_node.children.append(Node(name, curr_node))
            else:  # Else, save the file
                [size, name] = line.strip().split(" ")
                curr_node.files.append(File(name, int(size)))


if __name__ == "__main__":
    root = Node("/")  # Don't lose the ref to root

    with open("input.txt", "r") as input_file:
        parse_commands(root, input_file)

    # Part 1:
    print(root.size)
    print(Node.target_sum)

    # Part 2:
    used_space = root.size
    available_space = 70_000_000 - used_space
    needed_space = 30_000_000
    space_to_be_freed = needed_space - available_space

    root.add_nodes_gt(space_to_be_freed)

    Node.target_children.sort(key=lambda x: x.size)
    print(Node.target_children[0])
