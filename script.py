from number_guessing_bot import is_number_correct, NumberGuessingBot as Bot


MSG = "Type 4-digits number with different digits:"
WRONG_NUMBER_MSG = "Wrong number, please type again:"
PLAYER_TURN_MSG = "Your turn"
BOT_TURN_MSG = "Bot's turn"


def run():
    print(MSG)
    player_number = input()

    while not is_number_correct(player_number):
        print(WRONG_NUMBER_MSG)
        player_number = input()
    
    print('Thanks, your number is ', player_number)
    print("Now, let's start. Remember to use 1.5 instead 1,5 when typing nondecimal number.")
    bot = Bot()

    while True:
        print(PLAYER_TURN_MSG)
        guess = input()
        while not is_number_correct(guess):
            print(WRONG_NUMBER_MSG)
            guess = input()
            
        print(bot.answer(guess))

        print(BOT_TURN_MSG)
        bot.guess()
    
run()