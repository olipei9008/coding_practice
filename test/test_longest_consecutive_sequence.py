from leetCodeMed.longestConsecutiveSequence.LCS import *
import json
import os
import pytest

test_datafile = os.getcwd() + "/leetCodeMed/longestConsecutiveSequence/lcs_data.json"
with open(test_datafile, "r") as datafile:
    test_data = json.load(datafile)

@pytest.mark.parametrize("test_dict", test_data)
def test_longest_consecutive_subsequence(test_dict):
    nums = test_dict["input"]
    solution = test_dict["output"]
    lcs_finder = LCS(nums)
    result = lcs_finder.find_len_lcs()
    assert result == solution

@pytest.mark.parametrize("test_dict", test_data)
def test_longest_consecutive_subsequence_optimal(test_dict):
    nums = test_dict["input"]
    solution = test_dict["output"]
    lcs_finder = LCS(nums)
    result = lcs_finder.find_len_lcs_optimal()
    assert result == solution