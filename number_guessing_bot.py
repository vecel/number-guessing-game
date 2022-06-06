from random import choice


def is_number_correct(str_number):
    if not str_number.isdecimal():          return False
    if not has_diffrent_digits(str_number): return False
    if start_with_zero(str_number):         return False
    if len(str_number) != 4:                return False
    return True

def start_with_zero(str_number):
    return str_number[0] == '0'

def has_diffrent_digits(str_number):
    for num in str_number:
        if str_number.count(num) > 1: return False
    return True

def generate_numbers():
    valid = []
    for i in range(1000, 10000):
        if is_number_correct(str(i)): valid.append(str(i))
    return valid


VALID_NUMBERS = generate_numbers()


class NumberGuessingBot:

    def __init__(self):
        self.number = choice(VALID_NUMBERS)
        self.possibilities = VALID_NUMBERS

    def answer(self, player_guess):
        """Return points value of guess"""
        points = 0.0
        for i in range(len(player_guess)):
            if self.number[i] == player_guess[i]:           points += 1
            elif self.number.count(player_guess[i]) == 1:   points += 0.5
        return points

    def guess():
        """Ask player about random, but possible, number then read answer and eliminate invalid numbers"""
        pass


        