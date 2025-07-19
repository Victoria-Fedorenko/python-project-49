import random

from brain_games.functions import check_answer, game_cycle, say_hi_and_get_name


def get_random_numbers_and_correct_gcd():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    random_numbers = f'{a} {b}'
    if a == 0:
        correct_answer = b
    elif b == 0:
        correct_answer = a
    else:
        while b > 0: 
            o = a % b
            a = b
            b = o
        correct_answer = a
    return random_numbers, str(correct_answer)
    

def gcd_game():

    name = say_hi_and_get_name()
    print('Find the greatest common divisor of given numbers.')
    game_cycle(check_answer, name, get_random_numbers_and_correct_gcd)


def main():

    gcd_game()


if __name__ == "__main__":
    
    main()