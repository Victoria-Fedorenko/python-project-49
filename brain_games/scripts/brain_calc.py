from brain_games.functions import say_hi_and_get_name, check_answer, game_cycle
from brain_games.games.calc_game import get_expression_and_correct_answer


def main():

    name = say_hi_and_get_name()
    print('What is the result of the expression?')
    game_cycle(check_answer, name, get_expression_and_correct_answer)


if __name__ == "__main__":
    
    main()