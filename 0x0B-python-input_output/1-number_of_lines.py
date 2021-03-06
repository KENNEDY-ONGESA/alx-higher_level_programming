#!/usr/bin/python3


def number_of_lines(filename=""):
    """Count number of lines in file
    Args:
        filename (str): string of path to file
    Returns:
        number of lines in file
    """
    nb_lines = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            nb_lines += 1
    return nb_lines

