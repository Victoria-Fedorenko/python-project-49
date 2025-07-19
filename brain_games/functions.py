
import prompt


def say_hi_and_get_name():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_answer(name, function):

    your_number, correct_answer = function()
    print(f'Question: {your_number}')
    your_answer = prompt.string('Your answer: ')
    if your_answer == correct_answer:
        return True, your_answer, correct_answer
    return False, your_answer, correct_answer


def game_cycle(check_answer, name, function):

    for i in range(3):
        check_result, user_answer, correct_answer = check_answer(name, function)
        if check_result is True:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}!')
        elif check_result is False:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            break