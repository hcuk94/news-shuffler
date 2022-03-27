import random


def shuffle_cut(data, output_count=3):
    output = []
    random.shuffle(data)
    i = 0
    for entry in data:
        if i < output_count:
            output.append(entry)
            i += 1
    return output
