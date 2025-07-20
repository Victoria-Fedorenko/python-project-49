import random


def get_random_number_and_correct_answer(): #  for brain_even.py

    random_int = random.randint(0, 1000)
    if random_int % 2 == 0:
        correct_answer = 'yes'
    else: 
        correct_answer = 'no'
    return str(random_int), correct_answer