from homework7.task3 import tic_tac_toe_checker


def test_unfinished():
    """
    Testing that not completed board is detected and that
    row of '-' is not treated as win
    """

    board = [
        ["-", "-", "-"],
        ["o", "-", "o"],
        ["x", "x", "x"]
    ]
    assert tic_tac_toe_checker(board) == "unfinished"


def test_x_wins_row():
    """
    Testing that 'x wins' in a row is determined correctly
    """

    board = [
        ["o", "x", "o"],
        ["x", "o", "o"],
        ["x", "x", "x"]
    ]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_o_wins_column():
    """
    Testing that 'o wins' in a column is determined correctly
    """

    board = [
        ["o", "x", "o"],
        ["x", "x", "o"],
        ["x", "o", "o"]
    ]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_o_wins_diagonal():
    """
    Testing that 'o wins' in a diagonal is determined correctly
    """

    board = [
        ["o", "x", "o"],
        ["x", "o", "x"],
        ["o", "x", "o"]
    ]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_draw():
    """
    Testing that 'x wins' are determined correctly
    """

    board = [
        ["o", "x", "o"],
        ["x", "o", "x"],
        ["o", "o", "x"]
    ]
    assert tic_tac_toe_checker(board) == "draw!"
