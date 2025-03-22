from arrays.subArraySum.SubArraySum import *
import json
import os
import pytest

test_datafile = os.getcwd() + "/arrays/subArraySum/subarray_data.json"
with open(test_datafile, "r") as datafile:
    test_data = json.load(datafile)

## This function tests the subarray sum BRUTE FORCE
@pytest.mark.parametrize("test_dict", test_data)
def test_index_subarray_sum_bruteforce(test_dict):
    array = test_dict["array"]
    target = test_dict["target"]
    solution = test_dict["solution"]
    subarraysum = SubArraySum(array, target)
    assert subarraysum.find_subarray_bruteforce() == solution

@pytest.mark.parametrize("test_dict", test_data)
def test_index_subarray_sum_sliding_window(test_dict):
    array = test_dict["array"]
    target = test_dict["target"]
    solution = test_dict["solution"]
    subarraysum = SubArraySum(array, target)
    assert subarraysum.find_subarray_sliding_window() == solution