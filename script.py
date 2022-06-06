from number_guessing_bot import is_number_correct, NumberGuessingBot as Bot

MSG = "Type 4-digits number with different digits:"
WRONG_NUMBER_MSG = "Wrong number, please type again:"

def run():
    print(MSG)
    player_number = input()

    while not is_number_correct(player_number):
        print(WRONG_NUMBER_MSG)
        player_number = input()
    
    print('Thanks, your number is ', player_number)
    bot = Bot()

run()