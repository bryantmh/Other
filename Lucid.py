import sys
import re
import copy


def longest_subsequence(grid, num_rows, num_cols):
    """
    Take a rectangular grid of numbers and find the length
    of the longest sequence.
    Return the length as an integer.
    """
    currLongest = []
    for row in range(0, num_rows):
        for col in range(0, num_cols):
            longestArray = [grid[row][col]]
            numArray = subRec(row, col, grid, longestArray, num_rows, num_cols)
            if len(numArray) > len(currLongest):
                currLongest = numArray
    print(currLongest)
    return 0


def subRec(row, col, grid, longestArray, num_rows, num_cols):
    arrayToReturn = []
    if col is not 0:
        if grid[row][col - 1] != -1 and abs(grid[row][col] - grid[row][col - 1]) > 3:# and grid[row][col - 1] not in longestArray:
            newGrid = copy.deepcopy(grid)
            newGrid[row][col] = -1
            newArray = longestArray.copy()
            newArray.append(newGrid[row][col - 1])
            tempArray = subRec(row, col - 1, newGrid, newArray, num_rows, num_cols)
            if len(arrayToReturn) < len(tempArray):
                arrayToReturn = tempArray
    if col is not num_cols - 1:
        if grid[row][col + 1] != -1 and abs(grid[row][col] - grid[row][col + 1]) > 3:# and grid[row][col + 1] not in longestArray:
            newGrid = copy.deepcopy(grid)
            newGrid[row][col] = -1
            newArray = longestArray.copy()
            newArray.append(newGrid[row][col + 1])
            tempArray = subRec(row, col + 1, newGrid, newArray, num_rows, num_cols)
            if len(arrayToReturn) < len(tempArray):
                arrayToReturn = tempArray
    if row is not 0:
        if grid[row - 1][col] != -1 and abs(grid[row][col] - grid[row - 1][col]) > 3:# and grid[row - 1][col] not in longestArray:
            newGrid = copy.deepcopy(grid)
            newGrid[row][col] = -1
            newArray = longestArray.copy()
            newArray.append(newGrid[row - 1][col])
            tempArray = subRec(row - 1, col, newGrid, newArray, num_rows, num_cols)
            if len(arrayToReturn) < len(tempArray):
                arrayToReturn = tempArray
    if row is not num_rows - 1:
        if grid[row + 1][col] != -1 and abs(grid[row][col] - grid[row + 1][col]) > 3:# and grid[row + 1][col] not in longestArray:
            newGrid = copy.deepcopy(grid)
            newGrid[row][col] = -1
            newArray = longestArray.copy()
            newArray.append(newGrid[row + 1][col])
            tempArray = subRec(row + 1, col, newGrid, newArray, num_rows, num_cols)
            if len(arrayToReturn) < len(tempArray):
                arrayToReturn = tempArray
    if col is not 0 and row is not 0:
        if grid[row - 1][col - 1] != -1 and abs(grid[row][col] - grid[row - 1][col - 1]) > 3:# and grid[row - 1][col - 1] not in longestArray:
            newGrid = copy.deepcopy(grid)
            newGrid[row][col] = -1
            newArray = longestArray.copy()
            newArray.append(newGrid[row - 1][col - 1])
            tempArray = subRec(row - 1, col - 1, newGrid, newArray, num_rows, num_cols)
            if len(arrayToReturn) < len(tempArray):
                arrayToReturn = tempArray
    if col is not num_cols - 1 and row is not 0:
        if grid[row - 1][col + 1] != -1 and abs(grid[row][col] - grid[row - 1][col + 1]) > 3:# and grid[row - 1][col + 1] not in longestArray:
            newGrid = copy.deepcopy(grid)
            newGrid[row][col] = -1
            newArray = longestArray.copy()
            newArray.append(newGrid[row - 1][col + 1])
            tempArray = subRec(row - 1, col + 1, newGrid, newArray, num_rows, num_cols)
            if len(arrayToReturn) < len(tempArray):
                arrayToReturn = tempArray
    if row is not num_rows - 1 and col is not 0:
        if grid[row + 1][col - 1] != -1 and abs(grid[row][col] - grid[row + 1][col - 1]) > 3:# and grid[row + 1][col - 1] not in longestArray:
            newGrid = copy.deepcopy(grid)
            newGrid[row][col] = -1
            newArray = longestArray.copy()
            newArray.append(newGrid[row + 1][col - 1])
            tempArray = subRec(row + 1, col - 1, newGrid, newArray, num_rows, num_cols)
            if len(arrayToReturn) < len(tempArray):
                arrayToReturn = tempArray
    if row is not num_rows - 1 and col is not num_cols - 1:
        if grid[row + 1][col + 1] != -1 and abs(grid[row][col] - grid[row + 1][col + 1]) > 3:# and grid[row + 1][col + 1] not in longestArray:
            newGrid = copy.deepcopy(grid)
            newGrid[row][col] = -1
            newArray = longestArray.copy()
            newArray.append(newGrid[row + 1][col + 1])
            tempArray = subRec(row + 1, col + 1, newGrid, newArray, num_rows, num_cols)
            if len(arrayToReturn) < len(tempArray):
                arrayToReturn = tempArray
    if (len(arrayToReturn) < len(longestArray)):
        return longestArray
    else:
        return arrayToReturn


def main():
    # textIn = ["33",
    #         "824",
    #         "061",
    #         "379"]
    # dims = [int(i) for i in textIn[0]]
    num_rows, num_cols = 3, 3
    # num_rows, num_cols = 2, 2
    # grid = [[int(i) for i in textIn] for _ in range(num_rows)]
    grid = [[8, 2, 4], [0, 6, 1], [3, 7, 9]]
    # grid = [[4, 2, 4], [0, 3, 1], [3, 7, 9]]
    # grid = [[1, 6, 2], [8, 3, 7], [4, 9, 5]]

    # grid = [[8, 2], [6, 3]]

    res = longest_subsequence(grid, num_rows, num_cols)
    # print(str(res) + "\n")


if __name__ == "__main__":
    main()