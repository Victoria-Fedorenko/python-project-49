from brain_games.functions import check_answer, game_cycle, say_hi_and_get_name
from brain_games.games.progression_game import get_progression_and_correct_answer   


def main():

    name = say_hi_and_get_name()
    print('What number is missing in the progression?')
    game_cycle(check_answer, name, get_progression_and_correct_answer)


if __name__ == "__main__":
    
    main()