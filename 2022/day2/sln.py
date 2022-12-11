
def get_pick_score(pick):
    if pick == "A" or pick == "X":
        # Rock
        return 1
    elif pick == "B" or pick == "Y":
        # Paper
        return 2
    else:
        # Scissors
        return 3

def get_outcome_score(desired_outcome):
    return (ord(desired_outcome) - 88) * 3 

"""
Opponent's pick \ Desired Outcome
    X, Y, Z
A ->C, A, B
B ->A, B, C
C ->B, C, A

From the table we conclude that:
- To win you pick the option that comes next
- To draw you pick the same option
- To lose you pick the option that comes before
"""

# Circular linked list
cll = ["A", "B", "C"]

def get_outcome(opponent_pick, self_pick):
    if opponent_pick == self_pick:
        return 3
    
    win = False

    if opponent_pick == "A":
        if self_pick == "B":
            win = True
        elif self_pick == "C":
            win = False
        
    if opponent_pick == "B":
        if self_pick == "A":
            win = False
        elif self_pick == "C":
            win = True
    
    if opponent_pick == "C":
        if self_pick == "A":
            win = True
        elif self_pick == "B":
            win = False
    
    return 6 if win else 0

def get_self_pick(opponent_pick, desired_outcome):    
    if desired_outcome == "Y":
        self_pick = opponent_pick
    elif desired_outcome == "X":
        self_pick = cll[cll.index(opponent_pick) - 1]
    else:
        self_pick = cll[(cll.index(opponent_pick) + 1) % 3]

    return self_pick

def normalize_pick(self_pick):
    """
    Shift X to A, Y to B and Z to C
    """
    ascii_pick = ord(self_pick)
    ascii_pick -= 23
    return chr(ascii_pick)

if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        total_score = 0

        for line in input_file:
            opponent_pick, desired_outcome = line.split()
            total_score += get_pick_score(get_self_pick(opponent_pick, desired_outcome))
            total_score += get_outcome_score(desired_outcome)

        print(total_score)