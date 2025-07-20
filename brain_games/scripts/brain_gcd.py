from brain_games.functions import check_answer, game_cycle, say_hi_and_get_name
from brain_games.games.gcd_game import get_random_numbers_and_correct_gcd
    

def main():

    name = say_hi_and_get_name()
    print('Find the greatest common divisor of given numbers.')
    game_cycle(check_answer, name, get_random_numbers_and_correct_gcd)


if __name__ == "__main__":
    
    main()