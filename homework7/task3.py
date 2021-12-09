"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from itertools import chain, groupby
from typing import List


def all_equal(iterable) -> bool:
    """
    Returns True if all the elements are equal to each other

    @param iterable:
    @return:
    """
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def check_diagonal(board: List[List]) -> bool:
    """
    This functions check if there is a winner in a diagonal
    @param board: list of rows
    @return: bool
    """
    return all_equal(row[i] for i, row in enumerate(board))


def check_if_completed(board: List[List]) -> bool:
    """
    This function check if board is not completed
    @param board: list of rows
    @return: True if completed, False otherwise
    """
    return next(filter(lambda x: x == "-", chain(*board)), None) is None


def tic_tac_toe_checker(board: List[List]):
    if not check_if_completed(board):
        return "unfinished"

    if check_diagonal(board):
        return f"{board[0][0]} wins!"

    columns_iter = iter(board)
    rows_iter = zip(*board)

    result = next(
        (
            x for x in chain(columns_iter, rows_iter)
            if all_equal(x)
        ),
        None
    )

    return f"{result[0]} wins!" if result else "draw!"
