import json
from os import path
from typing import Tuple, List

PATH_ROOT = "data"
PATH_TRAIN = path.join(PATH_ROOT, "train.json")
PATH_TEST = path.join(PATH_ROOT, "test.json")
PATH_VALIDATION = path.join(PATH_ROOT, "valid.json")


def parse_data() -> Tuple[List, List, List]:
    """
    :return: train, test, validation
    """
    with open(PATH_TRAIN) as file:
        train = json.load(file)
    with open(PATH_TEST) as file:
        test = json.load(file)
    with open(PATH_VALIDATION) as file:
        validation = json.load(file)
    return train, test, validation


def get_data_as_lists() -> Tuple[Tuple[List, List], Tuple[List, List], Tuple[List, List]]:
    """
    :return: train, test, validation. Formatted like (list of codes, list of correct comments)
    """
    data = parse_data()
    train = ([], [])
    test = ([], [])
    validation = ([], [])
    for line in data[0]:
        train[0].append(line["code"])
        train[1].append(line["nl"])
    for line in data[1]:
        test[0].append(line["code"])
        test[1].append(line["nl"])
    for line in data[2]:
        validation[0].append(line["code"])
        validation[1].append(line["nl"])
    return train, test, validation

get_data_as_lists()