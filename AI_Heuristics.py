import random

import numpy as np, math
from copy import deepcopy
from AI_Movement import free_cells

COUNT_X = 4
COUNT_Y = 4

pattern = [[0, 0, 1, 3],
           [0, 1, 3, 5],
           [1, 3, 5, 15],
           [3, 5, 15, 30]]

corner = [[0.0, 0.0, 0.1, 0.1],
          [0.0, 0.1, 0.1, 0.3],
          [0.1, 0.1, 0.3, 0.5],
          [0.1, 0.3, 0.5, 1]]


def heuristics(grid, num_empty):
    """
    This function scores the grid based on the algorithm implemented
    so that the maximize function of AI_Minimax can decide which branch
    to follow.
    """
    grid = np.array(grid)
    score = 0


    # TODO: Implement your heuristics here.
    # You are more than welcome to implement multiple heuristics
    # p_score = pattern_score(grid)
    m_score = mono_score(grid)
    # penalty = penalty_score(grid)
    # corner = largest_in_corner(grid)
    # Weight for each score

    # Weights
    empty_weight = 100000
    mono_weight = 100000
    pattern_weight = 1000


    # scoring
    # score += pattern_score(grid) * pattern_weight
    score += mono_weight if m_score else -mono_weight
    score += num_empty * empty_weight

    return score


def smoothness(grid):
    score = 0
    pass


def mono_score(grid):
    score = 0
    # Ensure the rows are either increasing or decreasing
    colsTopBottom = all([is_increasing(grid[:, i]) for i in range(COUNT_X)])
    colsBottomTop = all([is_decreasing(grid[:, i]) for i in range(COUNT_X)])

    rowsLeftRight = all([is_increasing(grid[i, :]) for i in range(COUNT_X)])
    rowsRightLeft = all([is_decreasing(grid[i, :]) for i in range(COUNT_X)])


    BRCorner = colsTopBottom or rowsLeftRight
    TRCorner = colsBottomTop or rowsLeftRight

    BLCorner = colsTopBottom or rowsRightLeft
    TLCorner = colsBottomTop or rowsRightLeft

    return BRCorner or TRCorner or BLCorner or TLCorner


def is_increasing(arr):
    last = arr[0]
    for i in range(1, COUNT_X):
        if last > arr[i]:
            return False
        last = arr[i]
    return True


def is_decreasing(arr):
    last = arr[0]
    for i in range(1, COUNT_X):
        if last < arr[i]:
            return False
        last = arr[i]
    return True


def pattern_score(grid):
    score = 0
    for x in range(4):
        for y in range(4):
            score += grid[x][y] * pattern[x][y]

    return score


def penalty_score(grid):
    penalty = 0
    for x in range(4):
        for y in range(4):
            curr_cell = grid[x][y]
            neighbors = surrounding_cells(x, y, grid)
            for cell in neighbors:
                i, j = cell
                penalty += abs(curr_cell - grid[i][j])
    return penalty


def adjacent_score(grid):
    max_value = 0
    values = {}
    for x in range(COUNT_X):
        for y in range(COUNT_Y):
            cell_val = grid[y][x]
            if max_value < cell_val and can_cell_be_merged(x, y, grid):
                if not values.get(cell_val):
                    values[cell_val] = 1
                else:
                    values[cell_val] *= cell_val
    return values


"""
Helper Functions
"""


def row_is_montonic(grid):
    rows = np.all(grid[:, 1:] >= grid[:, :-1], axis=1)
    mono_rows = np.count_nonzero(rows)
    return mono_rows, mono_rows != 0


def column_is_montonic(grid):
    cols = np.all(grid[:, 1:] >= grid[:, :-1], axis=0)
    mono_cols = np.count_nonzero(cols)
    return mono_cols, mono_cols != 0


def surrounding_cells(x, y, grid):
    cells = [(x - 1, y - 1),  # Top left 0
             (x - 1, y),  # Top 1
             (x - 1, y + 1),  # Top right 2
             (x, y + 1),  # Right 3
             (x + 1, y + 1),  # Bottom right 4
             (x + 1, y),  # Bottom 5
             (x + 1, y - 1),  # Bottom Left 6
             (x, y - 1)  # Left 7
             ]

    i = 0
    while i < len(cells):
        cell = cells[i]
        x, y = cell
        if x < 0 or x > COUNT_X - 1:
            cells.remove(cell)
            i -= 1
        elif y < 0 or y > COUNT_Y - 1:
            cells.remove(cell)
            i -= 1
        i += 1

    return cells


def can_cell_be_merged(x, y, grid):
    """Checks if a cell can be merged, when the """
    value = grid[y][x]
    if y > 0 and grid[y - 1][x] == value:  # Cell above
        return True
    if y < COUNT_Y - 1 and grid[y + 1][x] == value:  # Cell below
        return True
    if x > 0 and grid[y][x - 1] == value:  # Left
        return True
    if x < COUNT_X - 1 and grid[y][x + 1] == value:  # Right
        return True
    return False


def adjacent(grid):
    score = 0

    for x in range(COUNT_X):
        for y in range(COUNT_Y):
            if can_cell_be_merged(x, y, grid):
                score += 1
    return score


def get_largest_value(grid):
    max_value = 0

    for x in range(COUNT_X):
        for y in range(COUNT_Y):
            if max_value < grid[y][x]:
                max_value = grid[y][x]

    return max_value


def largest_in_corner(grid):
    largest = get_largest_value(grid)

    if grid[0][0] == largest:
        return True

    if grid[0][3] == largest:
        return True

    if grid[3][0] == largest:
        return True

    if grid[3][3] == largest:
        return True
    return False
