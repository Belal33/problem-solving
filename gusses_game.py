####################################################################
"""
5- Gusses game
        ● Your game generates a random number and gives only 10 tries for the user to
                guess that number.
        ● Get a user input and compare it with the random number
        ● Display a hit message to the user in case the use number is smaller or bigger of
                the random number
        ● If the user type number is out of range(100), display a message that is not allowed
                and don’t count this as try.
        ● If user type a number that has been entered before, display a hint message and
                don’t count this as try
        ● In case the user entered a correct number within the 10 tries, display a
                congratulations message and let your application guess another random number
                with the remain number of tries
        ● If the user finishes all his tries, display a message to ask him if he wants to play
                again or not.
"""
from random import randint


class GussesGame:

    def __init__(self, level: int):
        self.__random_number = randint(0, 100)
        self.max_tries = 10
        self.tries_count = 0
        self.level = level
        self.user_input = None

    def game_intro(self):
        print("#################################################")
        print(f"############ Start New Round [level:{self.level}] ###########")
        print("#################################################")

    def game_outro(self):
        print("##############################################")
        print(f"################ Game End ###################")
        print("#############################################")

    def validate_user_input(self, _input):
        try:
            _input = int(_input)
            if _input not in range(101):
                self.get_user_input(
                    f" [Invalide input<{_input}> The Number must be in range 0 : 100]"
                )

        except:
            self.get_user_input(f" [Invalide input<{_input}> Must be a Number]")

    def hint_message(self, message):
        print("")
        print("═" * 40)
        print(f"║ Tries Left: {10 - self.tries_count} - Last Input: {self.user_input}		║")
        print("║" + " " * 38 + "║")
        print(f"║ Hint->[{message}]		║")
        print("═" * 40)

    def get_user_input(self, validation_message=None):
        message = (
            f"Gusse{validation_message}: "
            if validation_message
            else f"Gusse [Number in range 0 : 100]: "
        )
        _input = input(message)
        self.validate_user_input(_input)
        self.user_input = int(_input)

    def round_iteration(self):
        if self.tries_count > self.max_tries - 1:
            print("***************> Game Over <***************")
            return
        self.get_user_input()
        self.tries_count += 1

        if self.user_input == self.__random_number:
            print("successfull gusse")

        elif self.user_input > self.__random_number:
            self.hint_message("write smaller number")
            self.round_iteration()
        else:
            self.hint_message("write bigger number")
            self.round_iteration()

    def start_new_round(self):
        self.__random_number = randint(0, 100)
        self.tries_count = 0
        self.level += 1
        self.round_iteration()

    def main(self):
        self.game_intro()
        self.start_new_round()
        start_new_round = (input("Are you Ready for New Round?<y/n>: ")).lower() == "y"
        if start_new_round:
            self.main()
        else:
            self.game_outro()


guss_game = GussesGame(1)
guss_game.main()


####################################################################
