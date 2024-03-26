from pathlib import Path

# Constants for the exercises:
WORKING_DIR = Path.cwd()
DATA_DIR = WORKING_DIR.parent / "10_file_io_exercise"


# 1. Sum numbers listed in a file
# Fill ____ pieces of the code below. sum_numbers_in_file function takes a input
# file path as argument, reads the numbers listed in the input file and returns
# the sum of those numbers. You can assume that each line contains exactly one
# numeric value.
def sum_numbers_in_file(input_file):
    total = 0
    with open(input_file) as f:
        for line in f:
            line = line.strip()  # Remove potential white space
            total += float(line)
    return total


in_file = DATA_DIR / "numbers.txt"
assert sum_numbers_in_file(in_file) == 189.5


# 2. Reading first word from each line of a file
# Implement find_first_words function which takes an input file path as argument.
# The function should find the first word of each line in the file and return
# these words as a list. If a line is empty, the returned list should contain an
# empty string for that line.

def find_first_words(input_file):
    first_words = []
    with open(input_file) as file:
        for line in file:
            if len(line) > 1:
                line = line.strip()
                first_words.append(line.split()[0])
            else:
                first_words.append("")
        file.close()
        return first_words


in_file1 = DATA_DIR / "simple_file.txt"
in_file2 = DATA_DIR / "simple_file_with_empty_lines.txt"

expected_file_1 = ["First", "Second", "Third", "And"]
assert find_first_words(in_file1) == expected_file_1

expected_file_2 = ["The", "", "First", "nonsense", "", "Then"]
assert find_first_words(in_file2) == expected_file_2
