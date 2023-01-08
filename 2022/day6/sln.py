"""
First, fill queue with 4 elements

Then, check for the uniqueness of those 4 elements,
----if there's repeated elements,
--------remove them until the first occurrence of the
--------repeated one is discarded
--------Then fill the queue again up to 4 elements

----if not,
--------grab one from the data stream
--------check for its existence in the queue
--------repeat last check
----if all 4 unique, return count

* Always keep the count of how many elements have been inserted to the queue
"""


def check_if_all_unique(queue: list) -> bool:
    """
    This function receives a list of characters, traverses the list and
    determines whether or not all items on the list are unique.
    Returns a boolean with the veredict.
    """
    unique_chars = {}
    for i in range(len(queue)):
        if queue[i] in unique_chars:
            return False
        else:
            unique_chars[queue[i]] = True
    return True


def fill_up_queue(queue: list, stream: str, size: int = 4) -> tuple[list, int]:
    """
    This function receives a list and a data stream (string) and must
    refill the list up to <size> length. It then returns the number of elements
    that were added to the list.
    """

    return ([], 0)


def remove_up_to_repeated(queue: list) -> list:
    """
    This function receives a list of characters with exactly one repeated item,
    it traverses the list from end to beginning to find the item that is
    repeated.
    Once it finds it, flushes the list up until the repeated item and BREAKS
    out of the loop.
    The modified list is returned.
    """
    for i in range(len(queue)-1, 0-1, -1):
        first_occurrence_index = queue.index(queue[i])
        if first_occurrence_index != i:
            for j in range(first_occurrence_index + 1):
                queue.pop(0)
            break
    return queue


def main() -> int:
    with open("input1.txt", "r") as input_file:
        data_stream = input_file.read()
        queue = []  # The queue that will hold the current 4 chars
        count = 0  # The count of chars scanned from the stream
        i = 0  # The index of the current char being scanned

        for i in range(4):
            queue.append(data_stream[i])
            count += 1
            i += 1

        while i < len(data_stream):
            # Check if current 4 are unique
            #   if so,
            #       return count

            # else,
            #   remove up to the repeated one
            #       refill the queue,
            if check_if_all_unique(queue):
                return count
            else:
                queue = remove_up_to_repeated(queue)
                items_to_add = 4 - len(queue)
                for j in range(items_to_add):
                    queue.append(data_stream[i])
                    i += 1
                    count += 1
        return count
    return 0


if __name__ == "__main__":
    print(main())
