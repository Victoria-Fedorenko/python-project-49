import random
from brain_games.functions import say_hi_and_get_name, check_answer, game_cycle

def get_progression_and_correct_answer():
    first_num = random.randint(0, 100)
    step = random.randint(1, 10)
    correct_list = []
    correct_list.append(first_num)
    for i in range(10):
        new_elem = correct_list[-1] + step
        correct_list.append(new_elem)
    index_to_get_rid_of = random.randint(0,9)
    correct_answer = correct_list[index_to_get_rid_of]
    question_list = []
    for i in correct_list:
        i_str = str(i)
        question_list.append(i_str)
    question_list[index_to_get_rid_of] = '..'
    question = ' '.join(question_list)
    return question, str(correct_answer)

def progression_game():

    name = say_hi_and_get_name()
    print('What number is missing in the progression?')
    game_cycle(check_answer, name, get_progression_and_correct_answer)


def main():

    progression_game()

if __name__ == "__main__":
    
    main()