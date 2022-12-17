"""
for each line in the input text
Analyze the first half of the characters
    Fill up a dictionary with the first half, each entry will be a letter
Analyze the second half
    For each letter, check whether it also shows up in the first half
        if so, you're done with that line
    
    Get the priority of the repeated letter and store it for later processing

Once you've parsed all the input lines
Sum all of the repeated letters' priorities
print the result
"""

from functools import reduce

def get_char_dict(line, start_idx=0, end_idx=None):
    if end_idx is None:
        end_idx = len(line)

    char_dict = {}
    for i in range(start_idx, end_idx):
        char_dict[line[i]] = True

    return char_dict

def get_repeated_item(line):
    half_idx = len(line) // 2
    first_half_dict = {}
    repeated_item = None

    # Read first half
    first_half_dict = get_char_dict(line, 0, half_idx)

    # Read second half
    for i in range(half_idx, len(line)):
        if line[i] in first_half_dict:
            repeated_item = line[i]
            break
        
    return repeated_item

def get_common_item(lines):
    # Store the common items between all three lines
    repeated_items = {}

    # Create a dict from the first line
    line1_dict = get_char_dict(lines[0])

    # Compare it with the second line
    for char in lines[1]:
        if char in line1_dict:
            repeated_items[char] = True
    
    # Compare the repeated items with the third line
    for char in lines[2]:
        if char in repeated_items:
            # Return the first character common between all three lines
            return char

def get_priority(item):
    ascii_value = ord(item)
    # If uppercase, subtract 
    if ascii_value >= 97:
        return ascii_value - 96
    else:
        return ascii_value - 38

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        priorities_so_far = []
        
        # Part 1
        #for line in input_file:
        #    priorities_so_far.append(get_priority(get_repeated_item(line)))
        
        # Part 2
        try:
            while True:
                lines = []
                for _ in range(3):
                    lines.append(next(input_file).rstrip('\n'))
                priorities_so_far.append(get_priority(get_common_item(lines)))
        except StopIteration:
            pass
        
        total_priority = reduce(lambda x, y: x+y, priorities_so_far)
        print(total_priority)    
        
