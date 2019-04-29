import json
from os import path
from typing import Tuple, List

PATH_ROOT = "data"
PATH_TRAIN = path.join(PATH_ROOT, "train.json")
PATH_TEST = path.join(PATH_ROOT, "test.json")
PATH_VALIDATION = path.join(PATH_ROOT, "valid.json")


def parse_data() -> Tuple[List, List, List]:
    with open(PATH_TRAIN) as file:
        train = json.load(file)
    with open(PATH_TEST) as file:
        test = json.load(file)
    with open(PATH_VALIDATION) as file:
        validation = json.load(file)
    return train, test, validation

parse_data()