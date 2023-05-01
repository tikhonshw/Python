from enum import Enum


class Choices(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

user_ch = Choices.Paper

if (user_ch == Choices.Rock):
    print('User selected rock')
elif (user_ch == Choices.Paper):
    print('User selected paper')

print(user_ch.value)
