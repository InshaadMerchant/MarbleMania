import sys

# Global Variables
Red_marbles = 0
Blue_marbles = 0
version = ""
firstPlayer = ""

R_point = 2
B_point = 3


def red_blue_nim_misere():
    global Red_marbles, Blue_marbles, firstPlayer, R_point, B_point

    Update_Player = firstPlayer.lower() == "computer"

    while Red_marbles > 0 and Blue_marbles > 0:  # Change condition to OR for misere version
        print(f"Initial Game State have {Red_marbles} red marbles, {Blue_marbles} blue marbles.")

        if Update_Player:
            print("Computer's turn...")
            move = minimax()
            pile = 'red' if move[1] == 0 else 'blue'
            marbles = move[0]
            print(f"Computer removes {marbles} marble from {pile} pile.")
            if move[1] == 0:
                Red_marbles -= marbles
            else:
                Blue_marbles -= marbles
        else:
            print("Human's turn...")
            while True:
                pile = input("Enter pile red or blue:- ").lower()
                if pile not in ['red', 'blue']:
                    print("Invalid pile. Try again.")
                elif (pile == "red" and Red_marbles == 0) or (pile == "blue" and Blue_marbles == 0):
                    print("No marble left in this pile. Try again.")
                else:
                    break
            while True:
                try:
                    marbles = int(input("Enter the number of marbles to remove (1 or 2): "))
                    if marbles not in [1, 2]:
                        print("Invalid input. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Try again.")

            print(f"Human removes {marbles} marble(s) from {pile} pile.")
            if pile == "red":
                Red_marbles -= marbles
            else:
                Blue_marbles -= marbles

        Update_Player = not Update_Player

    if Red_marbles == 0 or Blue_marbles == 0:  # Check if a pile is empty
        if Update_Player:  # If it's the computer's turn and a pile is empty
            winner = "computer"
            if Red_marbles == 0:
                curr_score = Blue_marbles * B_point
            else:
                curr_score = Red_marbles * R_point

        else:  # If it's the human's turn and a pile is empty
            winner = "human"
            if Red_marbles == 0:
                curr_score = Blue_marbles * B_point
            else:
                curr_score = Red_marbles * R_point

    print(f"Our Winner is {winner} with a score of {curr_score}")
    print("\nGame is finished....")


def red_blue_nim():
    global Red_marbles, Blue_marbles, firstPlayer, R_point, B_point

    Update_Player = firstPlayer.lower() == "computer"

    while Red_marbles > 0 and Blue_marbles > 0:
        print(f"Initial Game State have {Red_marbles} red marbles, {Blue_marbles} blue marbles.")

        if Update_Player:
            print("Computer's turn...")
            move = minimax()
            pile = 'red' if move[1] == 0 else 'blue'
            marbles = move[0]
            print(f"Computer removes {marbles} marble from {pile} pile.")
            if move[1] == 0:
                Red_marbles -= marbles
            else:
                Blue_marbles -= marbles
        else:
            print("Human's turn...")
            while True:
                pile = input("Enter pile red or blue:- ").lower()
                if pile not in ['red', 'blue']:
                    print("Invalid pile. Try again.")
                elif (pile == "red" and Red_marbles == 0) or (pile == "blue" and Blue_marbles == 0):
                    print("No marble left in this pile. Try again.")
                else:
                    break
            while True:
                try:
                    marbles = int(input("Enter the number of marbles to remove (1 or 2): "))
                    if marbles not in [1, 2]:
                        print("Invalid input. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Try again.")

            print(f"Human removes {marbles} marble(s) from {pile} pile.")
            if pile == "red":
                Red_marbles -= marbles
            else:
                Blue_marbles -= marbles

        Update_Player = not Update_Player

    print("\nGame is finished....")

    # Determine winner
    if Red_marbles == 0 or Blue_marbles == 0:  # Check if a pile is empty
        if Update_Player:  # If it's the computer's turn and a pile is empty
            winner = "human"
            if Red_marbles == 0:
                curr_score = Blue_marbles * B_point
            else:
                curr_score = Red_marbles * R_point

        else:  # If it's the human's turn and a pile is empty
            winner = "computer"
            if Red_marbles == 0:
                curr_score = Blue_marbles * B_point
            else:
                curr_score = Red_marbles * R_point
        print(f"Our Winner is {winner} with a score of {curr_score}")


# Minimax algorithm Part 1 without alpha-beta pruning
def minimax():
    global Red_marbles, Blue_marbles

    result = [0, 0]
    maxEval = float('-inf')
    minEval = float('inf')

    for i in range(1, 3):  # Update the range to include 1 to 2 marbles
        for j in range(2):
            if (j == 0 and Red_marbles == 1) or (j == 1 and Blue_marbles == 1):
                continue  # If a pile has 1 marble left, skip this pile
            if (j == 0 and Red_marbles == 2) or (j == 1 and Blue_marbles == 2):
                continue  # If a pile has 2 marbles left, skip this pile
            if (j == 0 and Red_marbles < Blue_marbles) or (j == 1 and Blue_marbles < Red_marbles):
                continue  # if a pile has lesser marbles than the other, skip that pile and choose another

            # Adjusting the condition to pick marbles from any pile if both have 1 or 2 marbles left
            if (Red_marbles == 1 or Red_marbles == 2) and (Blue_marbles == 1 or Blue_marbles == 2) and (
                    Red_marbles < Blue_marbles):
                red_count = i
            else:
                red_count = i if j == 0 else 0

            # red_count = i if j == 0 else 0
            blue_count = i if j == 1 else 0
            newRed_marbles = Red_marbles - red_count
            newBlue_marbles = Blue_marbles - blue_count
            eval_val = alpha_beta_minimax(newRed_marbles, newBlue_marbles, float('-inf'), float('inf'), False)
            if eval_val > maxEval:
                maxEval = eval_val
                result = [i, j]
            else:
                minEval = eval_val
                result = [i, j]

    return result


# Minimax algorithm Part 2 with alpha-beta pruning
def alpha_beta_minimax(red_marbles, blue_marbles, alpha, beta, maximizingPlayer):
    if red_marbles == 0 or blue_marbles == 0:
        return (R_point * red_marbles) + (B_point * blue_marbles)

    if maximizingPlayer:
        maxEval = float('-inf')
        for i in range(1, 2):
            for j in range(0, 1):
                if (j == 0 and red_marbles == 0) or (j == 1 and blue_marbles == 0):
                    continue
                newRed_marbles = red_marbles - i if j == 0 else 0
                newBlue_marbles = blue_marbles - i if j == 1 else 0
                eval_val = alpha_beta_minimax(newRed_marbles, newBlue_marbles, alpha, beta, False)
                maxEval = max(maxEval, eval_val)
                alpha = max(alpha, eval_val)
                if beta <= alpha:
                    break
            return maxEval
    else:
        minEval = float('inf')
        for i in range(1, 2):
            for j in range(0, 1):
                if (j == 0 and red_marbles == 0) or (j == 1 and blue_marbles == 0):
                    continue
                newRed_marbles = red_marbles - i if j == 0 else 0
                newBlue_marbles = blue_marbles - i if j == 1 else 0
                eval_val = alpha_beta_minimax(newRed_marbles, newBlue_marbles, alpha, beta, True)
                minEval = min(minEval, eval_val)
                beta = min(beta, eval_val)
                if beta <= alpha:
                    break
            return minEval


def main():
    global Red_marbles, Blue_marbles, firstPlayer, version

    # Set game parameters
    Red_marbles = int(sys.argv[1])
    Blue_marbles = int(sys.argv[2])
    version = sys.argv[3].lower()
    firstPlayer = sys.argv[4].lower()

    if version == "standard":
        red_blue_nim()
    else:
        red_blue_nim_misere()


if __name__ == "__main__":
    main()
