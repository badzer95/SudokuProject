How to Play Sudoku with the Script

1. Run the Script
Execute the script in a Python environment. This will launch the game menu.


2. Game Menu
You will be presented with three options:

New Game
How to Play
Exit


3. Start a New Game
Select Option 1 to start a new game.
A new Sudoku puzzle will be generated and displayed.


4. Playing the Game
The script will display the Sudoku grid with some cells pre-filled.
Your task is to fill in the empty cells with numbers from 1 to 9.

Input Process:
Row Number: The script will prompt you to enter the row number (1-9).
Column Number: Next, you will be asked to enter the column number (1-9).
Number: Finally, you will input the number (1-9) you want to place in the specified cell.
The script will check the validity of your input and whether it matches the solution.

If the number is incorrect, it will count as a mistake.
The game continues until you successfully complete the grid without errors.
If during the input process you make a mistake, you can cancel the current input
by inputing 0 for either the row number, column number, or cell number. Your input
for that round will not count as a mistake or as a correct answer.


5. Game Completion
Once the grid is correctly filled, the script will congratulate you and indicate that the puzzle is complete.


6. Additional Options
How to Play (Option 2): This option will explain you how to play the game.
Exit (Option 3): Exits the game.

Summary of Functions
GridMaker: Creates an empty 9x9 Sudoku grid.
IsValid: Checks if placing a number in a specific cell is valid according to Sudoku rules.
EmptyLocationFinder: Finds the next empty cell in the grid.
SudokuSolver: Solves the Sudoku puzzle using backtracking.
SudokuMaker: Generates a complete, solved Sudoku grid.
SudokuUnsolver: Removes numbers from the solved grid to create a playable puzzle.
GridBuilder: Prints the current state of the Sudoku grid.
WinChecker: Checks if the player's grid matches the solved grid.
GridInputChecker, AnsInputChecker, GridChanger: Handle user input and update the grid accordingly.
Running the Game
To play the game, simply run the script in a Python environment, follow the prompts, and enjoy solving the Sudoku puzzle!
