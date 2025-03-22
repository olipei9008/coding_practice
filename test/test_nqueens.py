from leetCodeHard.nQueens.NQueens import *
import pytest
import json
import os

test_datafile = os.getcwd() + "/leetCodeHard/nQueens/nqueens_data.json"
with open(test_datafile, "r") as datafile:
    test_data = json.load(datafile)

@pytest.mark.parametrize("test_dict", test_data)
def test_nqueens_basic(test_dict):
    n = test_dict["n"]
    solution = test_dict["output"]
    nqueens_calc = NQueens(n)
    nqueens = nqueens_calc.nqueens_basic()
    assert nqueens == solution