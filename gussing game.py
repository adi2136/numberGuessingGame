import random


class NumberGuessingGame:
    def __init__(number):       
        number.LOWER = 1
        number.HIGHER = 10   
    def get_random_number(number):
        return random.randint(number.LOWER, number.HIGHER)  
    def start(number):       
        random_number = number.get_random_number()
        print(
            "Guess the random number from 1 to 10")       
        chances = 5
        while True:
            user_number = int(input("Enter the guessed number: "))
            if user_number == random_number:
                print(
                    " you won the game!")             
            elif user_number < random_number:
                print(" Your number is less than the random number")
                chances=chances-1
            else:
                print(" Your number is greater than the random number")
                chances=chances-1
            if(chances<=0):
                print("you lose the game")
numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()