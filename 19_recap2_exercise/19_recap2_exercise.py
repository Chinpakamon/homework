# 1. Rock-paper-scissors
# Implement rock_paper_scissors function which takes the player's
# rock-paper-scissors choice as an input (as integer), randomly selects the
# choice of the computer and reveals it (prints) and finally announces (prints)
# the result. The function should return PLAYER_WINS, COMPUTER_WINS or TIE.
import random

# Constants, you should use these in your implementation
ROCK = 1
PAPER = 2
SCISSORS = 3

PLAYER_WINS = "Player wins!! Woop woop!"
COMPUTER_WINS = "Robocop wins :-("
TIE = "It's a tie!"


def rock_paper_scissors(player):
    computer = random.randint(1, 3)
    if player == computer:
        print("Computer choice: ", computer)
        print("It's a tie!")
        return TIE
    elif (player == ROCK and computer == SCISSORS) or (
            player == PAPER and computer == ROCK) or (
            player == SCISSORS and computer == PAPER):
        print("Computer choice: ", computer)
        print("Player wins!! Woop woop!")
        return PLAYER_WINS
    else:
        print("Computer choice: ", computer)
        print("Robocop wins :-(")
        return COMPUTER_WINS


def play_rps():
    print("Welcome to play rock-paper-scissors")
    print("The options are:\nrock: 1\npaper: 2\nscissors: 3")

    result = TIE
    while result == TIE:
        player_choice = input("Give your choice\n")

        if not player_choice in ["1", "2", "3"]:
            print("Invalid choice")
            continue

        result = rock_paper_scissors(int(player_choice))


if __name__ == "__main__":
    play_rps()


# 2. Data analyzer
# Implement DataAnalyzer class which has the following specification:

# __init__ takes one argument which is a path to the file to be analyzed
# total_samples method returns the amount of the data samples in the file
# average method returns the average of the data samples in the file
# median method returns the median of the data samples in the file
# max_value method returns the maximum value of the data samples in the file
# min_value method returns the minimum value of the data samples in the file
# create_report method returns a report (string) of the file in the following
# format:
# Report for <filename>
# samples: x
# average: x.xx
# median: xx.xx
# max: xx.xx
# min: x.xx
# Note that average, median, max, and min should be presented with two decimal
# places in the report.

# The format of the input file is comma separated and the file contains only
# numeric values.

# If there is no data in the input file (empty file), NoData exception should be
# raised. Note: NoData should be your custom exception.

class NoData(Exception):
    pass


class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._read_data()

    def _read_data(self):
        with open(self.file_path, 'r') as file:
            data = file.read().strip()
            if not data:
                raise NoData("No data found in the file.")
            return [float(x) for x in data.split(',')]

    def total_samples(self):
        return len(self.data)

    def average(self):
        return sum(self.data) / len(self.data) if self.data else 0

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        return (sorted_data[mid] + sorted_data[~mid]) / 2 if n % 2 == 0 else \
            sorted_data[mid]

    def max_value(self):
        return max(self.data) if self.data else 0

    def min_value(self):
        return min(self.data) if self.data else 0

    def create_report(self):
        report = f"Report for random_data.txt\n"
        report += f"samples: {self.total_samples()}\n"
        report += f"average: {self.average():.2f}\n"
        report += f"median: {self.median():.2f}\n"
        report += f"max: {self.max_value():.2f}\n"
        report += f"min: {self.min_value():.2f}"
        return report


from pathlib import Path

WORKING_DIR = Path.cwd()
DATA_DIR = WORKING_DIR.parent / "19_recap2_exercise"
DATA_FILE = DATA_DIR / "random_data.txt"

da = DataAnalyzer(DATA_FILE)

assert da.total_samples() == 10
assert da.average() == 5.5
assert da.median() == 5.5
assert da.max_value() == 10
assert da.min_value() == 1

report = da.create_report()
print(report)

expected_report = (
    "Report for random_data.txt\n"
    "samples: 10\n"
    "average: 5.50\n"
    "median: 5.50\n"
    "max: 10.00\n"
    "min: 1.00"
)
assert report == expected_report

EMPTY_FILE = DATA_DIR / "empty_file.txt"
try:
    da_empty = DataAnalyzer(EMPTY_FILE)
except NoData:
    print("All ok :)")
else:  # There was no exception
    assert False
