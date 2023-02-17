#!/usr/bin/env python3

import collections

RESULT_TIE = 0
RESULT_PLAYER_1 = 1
RESULT_PLAYER_2 = 2

# A mapping of a turns to a result
rules = {
    'RR': RESULT_TIE, 
    'RP': RESULT_PLAYER_2, 
    'RS': RESULT_PLAYER_1,
    'PR': RESULT_PLAYER_1,
    'PP': RESULT_TIE,
    'PS': RESULT_PLAYER_2,
    'SR': RESULT_PLAYER_2,
    'SP': RESULT_PLAYER_1,
    'SS': RESULT_TIE,
}

# A mapping of short choice code to human-readable string
choices = {
    'R': "Rock", 
    'P': "Paper", 
    'S': "Scissors",
}

# A mapping of result code to human-readable result
results = {
    RESULT_TIE: "{0} and {1} tie, everyone loses\n", 
    RESULT_PLAYER_1: "{0} beats {1}, player 1 wins!\n", 
    RESULT_PLAYER_2: "{1} beats {0}, player 2 wins!\n",
}

# Score player choices
def score(choice_1, choice_2):
    return rules[choice_1 + choice_2] 

# Gather input for a player's turn
def turn(player_number):
    choice = None
    while (choice == None):
        choice = input("Player {} [R,P,S]? ".format(player_number)).upper()
        if not choice in choices:
            print("Enter R for rock, P for paper, or S for scissors")
            choice = None
        return choice

while (True):
    choice_1 = turn(1)
    choice_2 = turn(2)
    result = score(choice_1, choice_2)
    print(results[result].format(choices[choice_1], choices[choice_2]))
