import random
from copy import deepcopy

def GridMaker() -> list[list[int]]:
    """
    Returns a list with 9 nested lists.
    Each nested list contains 9 elements.
    Sets each of a 9 elements equal to 0.
    """
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(0)
        grid.append(row)
    return grid

def ZeroChecker(grid:list[list[int]]) -> bool:
    """
    Returns True if there is a 0 in the grid, otherwise it returns False.
    This function is no longer needed in newer versions of the code.
    This function has been replaced by EmptyLocationFinder (see bellow).
    It is left here for documentation purposes.
    This function may be safely removed in this version of the code.
    """
    for row in grid:
        for number in row:
            if number == 0:
                return True
    return False

def IsValid(num:int, xAxis:int, yAxis:int, grid:list[list[int]]) -> bool:
    """
    Checks if the added number does not violate the grid

    Parameters:
    num (int) = the number to be checked
    xAxis (int) = column coordinate
    yAxis (int) = row coordinate
    grid (2D list) = the full 9x9 grid in nested list form
    """
    if num in grid[yAxis]: #Row Validity Check
        return False
    for i in range(9): #Column Validity Check
        if grid[i][xAxis] == num:
            return False
    xStart = (xAxis // 3) * 3 #Starting X Coordinate for 3x3 grid
    yStart = (yAxis // 3) * 3 #Starting Y Coordinate for 3x3 grid
    for i in range(3): #3x3 Grid Validity Check
        for j in range(3):
            if grid[yStart + i][xStart + j] == num:
                return False
    return True

def EmptyLocationFinder(grid:list[list[int]]) -> tuple[int]:
    """
    Finds the next empty location on the grid.
    This function searches row by row from from top to bottom.
    In each row the function searches from left to right.
    Returns the x and y coordinates for the first 0 it finds.
    """
    for yAxis in range(9):
        for xAxis in range(9):
            if grid[yAxis][xAxis] == 0:
                return xAxis, yAxis
    return None

def SudokuSolver(grid:list[list[int]]) -> bool:
    """
    Uses recursion to solve the grid cell by cell. This function 
    is basically the core of the entire program and everything else
    has been developed around this funtion.
    """
    location = EmptyLocationFinder(grid) #Nearest empty location
    if location == None:
        return True #Grid Fully Solved
    xAxis, yAxis = location #X = row number; Y = column number
    numList = list(range(1,10)) #[1,2,3,4,5,6,7,8,9]
    random.shuffle(numList)
    for num in numList:
        if IsValid(num, xAxis, yAxis, grid): #Validity Check
            grid[yAxis][xAxis] = num
            if SudokuSolver(grid):
                return True
            grid[yAxis][xAxis] = 0 #Backtracking
    return False

def SudokuMaker() -> list[list[int]]:
    """
    Combines two functions in order to create a fully solved grid.
    The returned grid will be in nested list form, where every
    sublist represents a row in Sudoku and each element of that
    sublist is an integer that represents a number in a cell
    """
    grid = GridMaker()
    SudokuSolver(grid)
    return grid

def SudokuUnsolver(grid:list[list[int]], limit:int = 48) -> list[list[int]]:
    """
    Takes in a fully solved 9x9 grid in nested list form.

    The funtion will randomly replace numbers in the grid
    with 0 (set to 0 = removing it from the grid).

    Limit (int) is the removal limit (the amount of numbers
    that will be removed from the grid).

    The function will remove numbers randomly until it reaches
    the specified removal limit.

    The default limit is set at 48 to leave in 33 numbers
    as clues (meduim difficulty).

    The limit CANNOT be set higher than 64 because a minimum
    of 17 numbers must remain in the grid as clues.

    The function preserves the input list (solved grid) in
    memory and only does manipulation on a copy of the list
    in a different location in memory. This is done to preserve
    the original solved list in memory for later use in the 
    main program.

    The main program only utalizes the default value of the
    limit (48), but the function was written this way to allow
    for future updates of the main program that can allow
    the user to select their own difficulty level.
    """
    while True:
        try:
            assert limit <= 64
            assert limit >= 0
        except AssertionError:
            print("Limit Error!")
            print("The limit must be between 0 and 64")
            limit = int(input("Enter the limit: "))
        except TypeError:
            print("Number Type Error!")
            print("Limit must be an integer (whole number)")
            limit = int(input("Enter the limit: "))
        except ValueError:
            print("Number Value Error!")
            print("Limit must be an integer (whole number)")
            limit = int(input("Enter the limit: "))
        else:
            break
    grid = deepcopy(grid) #Preserving the original grid in memory
    removedNumsCount = 0
    while removedNumsCount < limit:
        xAxis = random.randint(0,8)
        yAxis = random.randint(0,8)
        if grid[yAxis][xAxis] != 0:
            grid[yAxis][xAxis] = 0
            removedNumsCount += 1
    return grid

def GridBuilder(grid:list[list[int]]) -> None:
    """
    I wrote this funtion 3 weeks before writing this docstring. And
    I am realizing as I am writing this that GUIBuilder would have 
    been a much more accurate name. Because this is what all this
    function does, it converts the grid from nested list form to a
    graphical representation that is very similar to the traditional
    way sudoku puzzles are displayed. This function does not create a
    true GUI but rather a pseudo-GUI represention where all the 
    graphics are actually text art that emulates a traditional 
    sudoku grid.
    This funtion is merely a way to display the numbers in the grid,
    It does NOT modify or change anything in the original grid.
    """
    print("     C1", "C2", "C3", "C4", sep = "  ", end = "  ")
    print("C5", "C6", "C7", "C8", "C9", sep = "  ")
    count = 1
    for row in grid:
        print("   ", end = "")
        print("+---" * 9, end = "+")
        print()
        print(f"R{count}", end = " ")
        for number in row:
            if number == 0:
                number = " "
            print(f"| {number} ", end = "")
        print("|")
        count += 1
    print("   ", "+---" * 9, sep = "", end = "+")
    print()

def WinChecker(unsolved:list[list[int]], solved:list[list[int]]) -> bool:
    """
    Returns True if the unsolved grid fully matches the solved grid.
    Otherwise, it returns False.
    """
    for rowIndex in range(9):
        for columnIndex in range(9):
            if unsolved[rowIndex][columnIndex] != solved[rowIndex][columnIndex]:
                return False
    return True

def GridInputChecker(indexType:str) -> int:
    """
    Ensures the user input for row and column values are within valid
    parameters.
    Also, since the main program uses both python list indecies (0 to 8) for
    calculations and manipulation and it uses row/column values (1 to 9) for
    user inputs, this function converts the row/column form from user inputs
    into python index form by subtracting 1 from the user's valid input.

    This function also allows the user to input 0. If the user does so to either
    the column value or row value or both, this will tell the code to ignore all
    inputs for that round. This is done to allow a user to cancel an input round
    in case they make a mistake of inputting wrong values. How this works is that
    by the user inputting 0, this will cause GridInputChecker() to return a -1
    value. This -1 value will be passed to AnsInputChecker() through the main 
    program. After that, AnsInputChecker() will return 0 and that will be passed
    to GridChanger(). GridChanger() will then ignore all inputs for that round and
    not make any changes to the grid.

    This function has an else statement that is only intended to be triggered for
    debugging purposes. It is designed to intentionally crash the program in order
    to notify me or future developers of a hidden coding/logical error.
    """
    indexType = indexType.upper()
    if indexType == "ROW":
        while True:
            try:
                index = int(input("Enter the row number: R"))
                assert index >= 1
                assert index <= 9
            except AssertionError:
                print("Assertion Error!")
                print("You must enter an integer between 1 and 9")
            except TypeError:
                print("Type Error!")
                print("You must enter an integer between 1 and 9")
            except ValueError:
                print("Value Error!")
                print("You must enter an integer between 1 and 9")
            else:
                break
        index -= 1 #Converting grid index to python list index
    elif indexType == "COLUMN":
        while True:
            try:
                index = int(input("Enter the column number: C"))
                assert index >= 1
                assert index <= 9
            except AssertionError:
                print("Assertion Error!")
                print("You must enter an integer between 1 and 9")
            except TypeError:
                print("Type Error!")
                print("You must enter an integer between 1 and 9")
            except ValueError:
                print("Value Error!")
                print("You must enter an integer between 1 and 9")
            else:
                break
        index -= 1 #Converting grid index to python list index
    else:
        print("Coding Error!")
        print("Check GridIndexInputChecker")
        print("This code will intentionally cause an out of range exception")
        return -50
    return index

def AnswerChecker(ans:int, rowIndex:int, colIndex:int, solvedGrid:list[list[int]], mistakeCount:int) -> tuple[bool,int]:
    """
    AnswerChecker() comapres the suggested answer to the real answer in the solved grid.
    It also keeps track of the total number of mistakes.
    """
    if solvedGrid[rowIndex][colIndex] == ans:
        print("Correct Answer :)")
        return True, mistakeCount
    else:
        mistakeCount += 1
        print("Wrong Answer :(")
        return False, mistakeCount

def AnsInputChecker(rowIndex:int, colIndex:int, solvedGrid: list[list[int]], mistakes:int) -> tuple[bool,int]:
    statement = """Enter the number you would like to input into the selected cell"""
    if rowIndex == -1 or colIndex == -1: #User choosing to cancel the input
        return 0, mistakes
    while True:
        try:
            print(statement)
            ans = int(input("Enter the number to input in the cell: "))
            assert ans >= 1
            assert ans <= 9
            validity, mistakes = AnswerChecker(ans, rowIndex, colIndex, solvedGrid, mistakes)
            assert validity
        except AssertionError:
            if ans == 0 or not validity:
                return 0, mistakes
            print("Assertion Error!")
            print("Your answer is wrong.")
            print("You must enter the correct integer between 0 and 9")
        except TypeError:
            print("Type Error!")
            print("You must enter an integer between 0 and 9")
        except ValueError:
            print("Value Error!")
            print("You must enter an integer between 0 and 9")
        else:
            break
    return ans, mistakes

def GridChanger(unsolvedGrid:list[list[int]], num:int, rowIndex:int, colIndex:int) -> None:
    """
    This function makes changes to the unsolved grid. If num = 0 it means the user elected
    to cancel this round of inputs, therefore this function will not make any changes.

    Please not that GridChanger() relies on other functions for input validation. If
    developers want to use this funtion directly then they need to be careful of not
    inputting an argument that might raise an exception or modify wrong portions of
    the grid.
    """
    if num > 0:
        unsolvedGrid[rowIndex][colIndex] = num

#The debugging code has be turned into notes (#):
#solvedGrid = SudokuMaker()
#print("Solved Grid:")
#for row in solvedGrid:
    #print(row)
#print()
#print("Unsolved Grid:")
#unsolvedGrid = SudokuUnsolver(solvedGrid)
#for row in unsolvedGrid:
    #print(row)
#print()

#Output script:
while True:
    print("..." * 6)
    print("***Sudoku Game***")
    print("..." * 6)
    print()
    print("Menu")
    print("(1) New Game")
    print("(2) How to Play")
    print("(3) Exit")
    while True:
        try:
            option = int(input("Enter a number corrosponding to an option: "))
            assert option >=1
            assert option <= 3
        except AssertionError:
            print("Assertion Error!")
            print("You must enter an integer between 1 and 3")
        except TypeError:
            print("Type Error!")
            print("You must enter an integer between 1 and 3")
        except ValueError:
            print("Value Error!")
            print("You must enter an integer between 1 and 3")
        else:
            break
    if option == 1:
        solvedGrid = SudokuMaker()
        unsolvedGrid = SudokuUnsolver(solvedGrid)
        mistakes = 0
        while not WinChecker(unsolvedGrid, solvedGrid):
            print()
            GridBuilder(unsolvedGrid)
            print(f"Mistakes: {mistakes}")
            print()
            rowNum = GridInputChecker("ROW")
            colNum = GridInputChecker("COLUMN")
            ansNum, mistakes = AnsInputChecker(rowNum, colNum, solvedGrid, mistakes)
            GridChanger(unsolvedGrid, ansNum, rowNum, colNum)
        print()
        GridBuilder(unsolvedGrid)
        print()
        print("Grid Complete. Yay! :)")
        print()
    elif option == 2:
        print("This page is under constuction")
        input("Press enter to continue")
    elif option == 3:
        break
    else:
        print("Coding Error!")
        print("Check else statement, output script")
print("Have a potato day!")