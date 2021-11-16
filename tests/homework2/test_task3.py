from homework2.task3 import combinations


def test_positive_combinations():
    assert combinations([1, 2, 4], [8, 9], [3, 4]) == [[1, 8, 3],
                                                       [1, 8, 4],
                                                       [1, 9, 3],
                                                       [1, 9, 4],
                                                       [2, 8, 3],
                                                       [2, 8, 4],
                                                       [2, 9, 3],
                                                       [2, 9, 4],
                                                       [4, 8, 3],
                                                       [4, 8, 4],
                                                       [4, 9, 3],
                                                       [4, 9, 4]]


def test_negative_combinations():
    assert combinations([], [], []) == []
