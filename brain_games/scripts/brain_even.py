import prompt
import random
from ..cli import welcome_user


def get_random_number_and_correct_answer():

    random_int = random.randint(0, 1000)
    if random_int % 2 == 0:
        correct_answer = 'yes'
    else: 
        correct_answer = 'no'
    return str(random_int), correct_answer

def check_answer(name):

    your_number, correct_answer = get_random_number_and_correct_answer()
    print(f'Question: {your_number}')
    your_answer = prompt.string(f'Your answer: ')
    if your_answer == correct_answer:
        return True, your_answer, correct_answer
    return False, your_answer, correct_answer
     

def even_game():

    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        check_result, user_answer, correct_answer = check_answer(name)
        if check_result is True:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}!')
        elif check_result is False:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            break


def main():

    even_game()

if __name__ == "__main__":
    
    main()
    

