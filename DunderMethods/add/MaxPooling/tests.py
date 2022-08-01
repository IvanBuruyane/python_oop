import json

from MaxPooling import MaxPooling
import pytest

with open("data.json", "r") as data:
    DATA = json.load(data)


def test_is_matrix_valid_function_success():
    """is_matrix_valid() function is a function that raises an error if matrix is incorrect"""
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
    MaxPooling.is_matrix_valid(matrix)


@pytest.mark.parametrize("matrix", [
    [[1, 2, 3, 4], [5, 6, 7, True], [9, 8, 7, 6], [5, 4, 3, 2]],
    1,
    "string",
    2.235,
    True,
    None,
    [[1, 2, 3, 4], [5, 6, 7, 34, 53], [9, 8, 7, 6], [5, 4, 3, 2]],
    [[1, 2, 3, 4], [5, 6, 7, 34], True, [5, 4, 3, 2]]
])
def test_is_matrix_valid_function_fail(matrix):
    with pytest.raises(ValueError) as e:
        MaxPooling.is_matrix_valid(matrix)
    assert str(e.value) == "Неверный формат для первого параметра matrix."


@pytest.mark.parametrize("matrix, size, step, result", DATA)
def test_max_pooling_success(matrix, size, step, result):
    mp = MaxPooling(size, step)
    res = mp(matrix)
    assert res == result
