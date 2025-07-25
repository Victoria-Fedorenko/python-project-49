import random


def get_random_int_and_correct_answer():

    random_int = random.randint(0, 100)
    if random_int <= 1:
        correct_answer = 'no'
    elif random_int == 2 or random_int == 3:
        correct_answer = 'yes'
    elif random_int > 2 and (random_int % 2) == 0:
        correct_answer = 'no'
    else:
        int_sqrt = int(random_int ** 0.5)
        divisors = []
        for i in range(3, int_sqrt):
            if random_int % i == 0:
                divisors.append(i)
        if len(divisors) > 0:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'
    return str(random_int), correct_answer