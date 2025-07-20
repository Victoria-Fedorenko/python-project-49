import random


def get_expression_and_correct_answer():

    operations_list = ['+', '-', '*']
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    random_operation = random.choice(operations_list)
    str_expression = f'{number_1} {random_operation} {number_2}'
    if random_operation == '+':
        correct_answer = number_1 + number_2
    elif random_operation == '-':
        correct_answer = number_1 - number_2
    elif random_operation == '*':
        correct_answer = number_1 * number_2
    return str_expression, str(correct_answer)