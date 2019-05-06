# Simple script to make the original data files valid json. Only to be run once
from os import path

filenames = ["train.json", "test.json", "valid.json"]
for filename in filenames:
    with open(path.join("data", filename)) as file:
        newlines = ["["]
        for line in file:
            newlines.append(line[:-1] + ",")
        newlines[-1] = newlines[-1][:-1]
        newlines.append("]")
    with open(path.join("data", filename), "w") as file2:
        for line in newlines:
            file2.write("%s\n" % line)
