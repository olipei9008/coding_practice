from arrays.countTriplets.CountTriplets import *
import pytest
import json
import os

test_datafile = os.getcwd() + "/arrays/countTriplets/triplets_data.json"
with open(test_datafile, "r") as datafile:
    test_data = json.load(datafile)

@pytest.mark.parametrize("test_dict", test_data)
def test_counting_triplets(test_dict):
    array = test_dict["array"]
    solution = test_dict["solution"]
    triplet_counter = CountTriplets(array)
    count = triplet_counter.count_triplets_nohash()
    assert count == solution