from io import StringIO

crates = {
    1: ['H', 'C', 'R'],
    2: ['B', 'J', 'H', 'L', 'S', 'F'],
    3: ['R', 'M', 'D', 'H', 'J', 'T', 'Q'],
    4: ['S', 'G', 'R', 'H', 'Z', 'B', 'J'],
    5: ['R', 'P', 'F', 'Z', 'T', 'D', 'C', 'B'],
    6: ['T', 'H', 'C', 'G'],
    7: ['S', 'N', 'V', 'Z', 'B', 'P', 'W', 'L'],
    8: ['R', 'J', 'Q', 'G', 'C'],
    9: ['L', 'D', 'T', 'R', 'H', 'P', 'F', 'S']
}


class Shipment:
    def __init__(self, crates):
        self.crates = crates

    def __str__(self):
        buf = StringIO()
        for index, stack in self.crates.items():
            buf.write(f"{index}, {stack}\n")
        return buf.getvalue()

    def move_crate(self, stack_from, stack_to):
        self.crates[stack_to].append(self.crates[stack_from].pop())

    def move_crates(self, count, stack_from, stack_to):
        for i in range(count):
            self.move_crate(stack_from, stack_to)

    def print_top_crates(self):
        for index, stack in self.crates.items():
            print(self.crates[index][-1], end="")
        print("")


if __name__ == "__main__":
    test_ship = Shipment(crates)

    with open("input.txt", "r") as input_file:
        for command in input_file:
            _, count_str, _, from_str, _, to_str = command.split(" ")
            test_ship.move_crates(int(count_str), int(from_str), int(to_str))
        print(test_ship)
        test_ship.print_top_crates()
