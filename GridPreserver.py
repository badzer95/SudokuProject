"Grid Preserver Test Script"

def GridPreserver(grid:list[list[int]]) -> list[list[int]]:
    gridCopy = list()
    for row in grid:
        rowCopy = list()
        for num in row:
            rowCopy += [num]
        gridCopy += [rowCopy]
    return gridCopy

originalGrid = [[1,2],[3,4]]
copyGrid = GridPreserver(originalGrid)
print(f"Original grid: {originalGrid}")
print(f"Copied Grid: {copyGrid}")

for rowIndex in range(len(originalGrid)):
    print("---" * 6)
    print(f"R{rowIndex}")
    print(f"original ID: {id(originalGrid[rowIndex])}")
    print(f"copy ID: {id(copyGrid[rowIndex])}")
    print("---" * 6)