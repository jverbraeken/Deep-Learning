# Simple script to make the original data files valid json. Only to be run once
import json
from os import path

from preprocess import parser

filenames = ["train.json", "test.json", "valid.json"]
for filename in filenames:
    with open(path.join("../data/original", filename)) as file:
        newlines = ["["]
        for line in file:
            newlines.append(line[:-1] + ",")
        newlines[-1] = newlines[-1][:-1]
        newlines.append("]")
    with open(path.join("../data/original_validated", filename), "w") as file2:
        for line in newlines:
            file2.write("%s\n" % line)

    with open(path.join("../data/original", filename)) as file:
        newlines = file.readlines()
    with open(path.join("../data/preprocessed", filename), "w") as file:
        file.write("[\n")
        for line in newlines:
            line = json.loads(line)
            if parser.is_valid_data(line):
                code = line["code"]
                comment = parser.beautify(line["nl"])
                file.write("%s,\n" % json.dumps({"code": code, "nl": comment}))
        file.write("]")
