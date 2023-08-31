
from random import *


def roll_two_dice():

    max_value = 6
    min_value = 1

    dice_1 = randint(min_value, max_value)
    dice_2 = randint(min_value, max_value)
    a = 'Rolling dice...\n' + f'Dice one: {dice_1}\n' + f'Dice two: {dice_2}\n' + f'Total: {dice_1 + dice_2}'
    print('Rolling dice...')
    print('Dice one: ', dice_1)
    print('Dice two: ', dice_2)
    print('Total: ', dice_1 + dice_2)
    return a


def roll_one_dice():

    max_value = 6
    min_value = 1

    print('Rolling dice...')
    dice_1 = randint(min_value, max_value)
    print(f'The value is: {dice_1}')
    b = 'Rolling dice...\n' + f'The value is: {dice_1}'
    return b
