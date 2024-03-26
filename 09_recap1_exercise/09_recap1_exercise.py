# 1. Super vowels
# Implement super_vowels function which takes a string as an argument and
# returns a modified version of that string. In the return value of super_vowels,
# all vowels should be in upper case whereas all consonants should be in lower
# case. The vowels are listed in the VOWELS variable.

VOWELS = ["a", "e", "i", "o", "u"]


def super_vowels(word):
    ans = []
    for i in range(len(word)):
        if word[i].lower() in VOWELS:
            ans += word[i].upper()
        else:
            ans += word[i].lower()
    return ''.join(ans)


assert super_vowels("hi wassup!") == "hI wAssUp!"
assert super_vowels("HOw aRE You?") == "hOw ArE yOU?"

# 2. Playing board
# Implement get_playing_board function which takes an integer as an argument.
# The function should return a string which resemples a playing board
# (e.g. a chess board). The board should contain as many rows and columns as
# requested by the interger argument. See the cell below for examples of
# desired behavior.

import math


def get_playing_board(num):
    board = []
    s = []
    a, b = ['*'], [' ']

    while len(a) < num:
        if a[-1] == '*' and len(b) < num:
            a += [' ']
        if a[-1] == ' ' and len(b) < num:
            a += ['*']

    while len(b) < num:
        if b[-1] == '*' and len(b) < num:
            b += [' ']
        if b[-1] == ' ' and len(b) < num:
            b += ['*']

    for i in range(num):
        board += [b]
        board += [a]

    for i in range(num):
        print(''.join(board[i]))


board_of_5 = " * * \n" "* * *\n" " * * \n" "* * *\n" " * * \n"

board_of_10 = (
    " * * * * *\n"
    "* * * * * \n"
    " * * * * *\n"
    "* * * * * \n"
    " * * * * *\n"
    "* * * * * \n"
    " * * * * *\n"
    "* * * * * \n"
    " * * * * *\n"
    "* * * * * \n"
)
print(board_of_5)
assert get_playing_board(5) == board_of_5
# assert get_playing_board(10) == board_of_10

print(get_playing_board(5))
