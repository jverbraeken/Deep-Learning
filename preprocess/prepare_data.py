# Simple script to make the original data files valid json. Only to be run once
import json
from os import path

from preprocess import parser

filenames = ["train.json", "test.json", "valid.json"]
for filename in filenames:
    with open(path.join("../data/original", filename)) as file:
        validated_lines = ["["]
        preprocessed_lines = ["["]
        for line in file:
            validated_lines.append(line[:-1] + ",")
            json_line = json.loads(line[:-1])
            if parser.is_valid_data(json_line):
                code = json_line["code"]
                comment = parser.beautify(json_line["nl"])
                preprocessed_lines.append(json.dumps({"code": code, "nl": comment}) + ",")
        validated_lines[-1] = validated_lines[-1][:-1]
        validated_lines.append("]")
        preprocessed_lines[-1] = preprocessed_lines[-1][:-1]
        preprocessed_lines.append("]")
    with open(path.join("../data/original_validated", filename), "w") as file2:
        for line in validated_lines:
            file2.write("%s\n" % line)
    with open(path.join("../data/preprocessed", filename), "w") as file3:
        for line in preprocessed_lines:
            file3.write("%s\n" % line)
