import sys
from random import randint

import constant


def ask_to_play():
    user_input = input("Please type \"P\" or \"Play\" to start playing, and \"Q\" or \"Quit\" to quit the game\n")
    if user_input.casefold() == "P".casefold() or user_input.casefold() == "Play".casefold():
        return True
    elif user_input.casefold() == "Q".casefold() or user_input.casefold() == "Quit".casefold():
        return False
    else:
        print("Error! No matching option found.")
        return ask_to_play()


def question():
    # num = randint(-sys.maxsize, sys.maxsize)
    num = randint(0, 20)
    return num


def check_int(num):
    try:
        int(num)
        return int(num)
    except ValueError:
        print("The value is not an integer, please input a new value:")
        answer = input()
        return check_int(answer)


def check_answer(number, answer):
    if answer > number:
        print("Your answer is too high")
    elif answer < number:
        print("Your answer is too low")
    else:
        print("Yay! You got right!\n")
        return 1
    return 0


def main():
    while ask_to_play():
        number = question()
        answer = input("Input an integer:\n")
        for i in range(constant.TIMES - 1, -1, -1):
            answer = check_int(answer)
            value = check_answer(number, answer)
            if value == 1:
                break
            if i != 0:
                print(f"You have {i} time(s) left\n")
                answer = input("Input an integer:\n")
            else:
                print("Sorry! You ran out of trials.")
                print(f"The answer is {number}. Better luck next time!\n")


main()
