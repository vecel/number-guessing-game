MSG = "Type 4-digits number with different digits:"
WRONG_NUMBER_MSG = "Wrong number, please type again:"

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

def run():
    print(MSG)
    player_number = input()

    while not is_number_correct(player_number):
        print(WRONG_NUMBER_MSG)
        player_number = input()
    
    print('Thanks, your number is ', player_number)

run()
