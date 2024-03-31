# MarbleMania

This code was written as part of my CSE 4308 class.

Inshaad Merchant

UTA ID: 1001861293

Programming Language used: Python 3.9.13

Omega Compatibility: No

For compilation and testing: Use PyCharm

How the Code is Structured:

1) `red_blue_nim_misere()`: This function manages the main game loop, handling turns between the human player and the computer player. It checks for empty piles at the beginning of each turn to determine if a player has won according to the misère version rules.

2) `red_blue_nim()`: This function manages the main game loop, handling turns between the human player and the computer player. It checks for empty piles at the end of the function to determine which player won according to the standard version rules.

3) `minimax()`: This function implements the minimax algorithm to find the optimal move for the computer player. It iterates through all possible moves and calculates the evaluation value for each move using alpha-beta pruning.

4) `alpha_beta_minimax()`: This function is a helper function for the minimax algorithm, implementing alpha-beta pruning. It recursively evaluates possible future game states while keeping track of alpha and beta values to optimize the search process.

5) `main()`: This function sets up the game parameters based on command-line arguments and then calls the `red_blue_nim_misere()` function or the red_blue_nim() function based on the version provided on command line

How to run the code:

Either press "Run" on PyCharm

Or On the terminal, type "python red_blue_nim.py 10 10 standard human" and press Enter to play game in standard version.

Or On the terminal, type "python red_blue_nim.py 10 10 misere human" and press Enter to play game in misere version.
