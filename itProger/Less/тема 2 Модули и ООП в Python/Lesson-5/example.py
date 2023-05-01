from enum import Enum


class Choices(Enum):
    Sweet = 1,
    Spicy = 2,
    Ice = 3,
    Hot = 4

user_choice = Choices.Hot

if(user_choice == Choices.Sweet):
    print("User selected sweets")
elif(user_choice == Choices.Hot):
    print("User selected hot")
