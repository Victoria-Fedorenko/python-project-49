from brain_games.functions import check_answer, game_cycle, say_hi_and_get_name
from brain_games.games.even_game import get_random_number_and_correct_answer


def main():

    name = say_hi_and_get_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_cycle(check_answer, name, get_random_number_and_correct_answer)
    

if __name__ == "__main__":
    
    main()
    

