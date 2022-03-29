import random


def shuffle_cut(data, output_count=3):
    """Randomises a list of data, then outputs the amount of values set in output_count"""
    output = []
    random.shuffle(data)
    i = 0
    for entry in data:
        if i < output_count:
            output.append(entry)
            i += 1
    return output
