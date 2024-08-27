import random as rnd
import sys


def check_guess(lucky_number: int, user_guess: str) -> str:
    '''
    Checks if user guess is valid,
    and if it is checks weather its is higher,
    lower or equal to the lucky_number
    '''

    try:
        guess: int = int(user_guess);
    except Exception as ex:
        raise ValueError;

    if guess > 100 or guess <1:
        raise ValueError("number out of range");
    elif guess > lucky_number:
        return "guess lower";
    elif guess < lucky_number:
        return "guess higher";
    else:
        return "BINGO!!!";

# ___requirements___:
# if user_guess is invalid, a ValueError is raised
# if user_guess is not in the 1 to 100 range a ValueError with the "number out of range" text
# if user_guess is equal to the lucky_number, a "BINGO!!!" massage is returned
# if user_guess is lower than the lucky_number, a "guess higher" massage is returned
# if user_guess is higher than the lucky_number, a "guess lower" massage is returned

def game_guessing_play():
    '''
    Plays the guessing game;
    :return:
    None;
    '''

    lucky_num: int = rnd.randint(1,100);
    while True:
        try:
            user_guess: str = input("Guess the lucky number(between 1 and 100): ");
            feedback: str = check_guess(lucky_num, user_guess);
            print(feedback);
            if feedback == "BINGO!!!":
                choice: str = input("Play another game (Y/N): ");
                if choice.upper() == "Y":
                    game_guessing_play();
                else:
                    sys.exit();

        except Exception as ex:
            print(ex);


