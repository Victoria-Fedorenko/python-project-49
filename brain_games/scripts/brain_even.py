import random

from brain_games.functions import check_answer, game_cycle, say_hi_and_get_name


def get_random_number_and_correct_answer():

    random_int = random.randint(0, 1000)
    if random_int % 2 == 0:
        correct_answer = 'yes'
    else: 
        correct_answer = 'no'
    return str(random_int), correct_answer


def even_game():

    name = say_hi_and_get_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_cycle(check_answer, name, get_random_number_and_correct_answer)


def main():

    even_game()


if __name__ == "__main__":
    
    main()
    

