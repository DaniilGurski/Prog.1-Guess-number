
import colorama
import os
import random
import time

from colorama import Fore, Back, Style

# Adding color to one text will not affect next text lines.
colorama.init(autoreset=True)

class GuessTheNumber:

    def __init__(self):
        self.win_record = 0
        self.default_guess_count = 7


    def generate_random_number(self):
        return random.randint(1, 100)


    def reduce_guess_number(self, guesses_left):
        guesses_left -= 1
        print(f"{Fore.WHITE}{guesses_left}{Fore.LIGHTBLACK_EX} / 7 guesses left.")
        return guesses_left


    def is_record_broken(self, finishing_time):
        if finishing_time < self.win_record or self.win_record == 0:
            return True
        return False


    def get_valid_input(self, prompt):
        while True:
            user_input = input(prompt)
            try: 
                return int(user_input)
            except:
                if user_input == "q": 
                    return user_input
                print(f"{Fore.LIGHTRED_EX}Your input must be a number or a valid command.\n")


    def create_time_display(self, finishing_time):
        # % 60 prevents numbers from going beyond 60.
        seconds = finishing_time % 60
        mintues = int(finishing_time / 60) % 60
        hours = int(finishing_time / 3600)

        # fills in the blank with zero, for example 1 turns to 01
        return f"{hours:02}:{mintues:02}:{seconds:02}"


    def show_game_results(self, game_results):
        os.system("cls")
        
        starting_time = game_results["game_start_time"]
        finishing_time = int(time.time() - starting_time) 
        finishing_time_display = self.create_time_display(finishing_time)

        correct_number = game_results["correct_number"]
        guesses_left = game_results["guesses_left"]

        is_win = game_results["is_win"]

        if not is_win:
            return print(f"\n{Fore.BLUE}You lost ! The number was {Fore.LIGHTCYAN_EX}{correct_number}\n")

        print(
        f"""
{Fore.LIGHTGREEN_EX}You won 🥇!
It took {finishing_time_display} for you to find the correct number
You saved {guesses_left} guesses.
        """
        )

        if self.is_record_broken(finishing_time):
            self.win_record = finishing_time
            return print("New record achived !")
    

    def main(self):
        game_start_time = time.time()
        game_win = False

        correct_number = self.generate_random_number()
        guesses_left = self.default_guess_count # 7

        while (guesses_left) and (not game_win):
            user_guess = self.get_valid_input(f"\n{Fore.LIGHTWHITE_EX}What is your guess ?: ")

            if user_guess == "q":
                return 

            elif user_guess == correct_number:
                game_win = True

            elif user_guess > correct_number:
                print(f"\n{Fore.LIGHTBLUE_EX}Go lower. ⬇")

            elif user_guess < correct_number:
                print(f"\n{Fore.LIGHTYELLOW_EX}Go higher ⬆")

            guesses_left = self.reduce_guess_number(guesses_left)
        
        # By creating a dict with all variables, I avoid passing a large number of arguments to the function.
        game_results = {
            "is_win": game_win, 
            "correct_number" : correct_number, 
            "game_start_time" : game_start_time,
            "guesses_left" : guesses_left
        }

        self.show_game_results(game_results)
        self.menu_command_selection("Type 's' to play again, 'q' for quiting: ")


    def menu_command_selection(self, prompt): 
        while True: 
            user_command = input(f"{Fore.LIGHTBLACK_EX}{prompt}").strip()

            if user_command == "s":
                break
            elif user_command == "q": 
                return
            print(f"{Fore.LIGHTRED_EX}Unknown command, Try again.")

        self.main()


    def menu(self): 
        os.system("cls")

        print(f"{Back.YELLOW}{Fore.BLACK}-- WELCOME TO THE GREAT \"GUESS NUMBER\" GAME ! --")
        print(
        f"""
The program will choose a number from {Fore.YELLOW}1 to 100{Fore.WHITE}.
Your goal is to find it! You have 7 guesses and unlimited time to think about the answer. 
However, you can try to beat your time record! Good luck :)
        """
        )

        self.menu_command_selection("Type 's' to start and 'q' for quiting: ")

game = GuessTheNumber()
game.menu()