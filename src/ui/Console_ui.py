from src.services.robot_services import *
from src.services.some_functions import *
from src.services.player_services import *
from texttable import Texttable

class UI:

    def Print_board(self, game_board):
        table = Texttable()

        header = [' ']
        first_element = 0

        for i in range(len(game_board[first_element])):
            header.append(str(i))
        table.header(header)

        for i in range(len(game_board)):
            table.add_row([str(i)] + game_board[i])

        print("")
        print(table.draw())
        print("")

    def Start(self):
        player_turn = True

        while True:
            try:
                length = input("Chose the board's length: ")
                width = input("Chose the board's width: ")
                maximum_valid_value = 10
                minimum_valid_value = 4

                length = length.strip()
                width = width.strip()

                if not Check_if_is_an_integer(length) or not Check_if_is_an_integer(width) or \
                        int(length) < minimum_valid_value or int(width) < minimum_valid_value\
                        or int(length) > maximum_valid_value or int(width) > maximum_valid_value:
                    raise ValueError
                else:
                    break

            except ValueError:
                print("")
                print("The length and width of the board must be integers bigger than 3 and smaller than 11 !")
                print("")

        while True:
            try:
                difficulty_level = input("Chose the difficulty level (1-easy, 2-hard): ")
                difficulty_level = difficulty_level.strip()
                easy_difficulty = str(1)
                hard_difficulty = str(2)

                if not Check_if_is_an_integer(difficulty_level) or (difficulty_level != easy_difficulty and difficulty_level != hard_difficulty):
                    raise ValueError
                else:
                    break

            except ValueError:
                print("Invalid difficulty level")

        game_board = obstruction_board(int(length), int(width))
        player = PlayerServices(game_board)
        robot = RobotServices(game_board, int(difficulty_level))

        while True:

            if player_turn:
                self.Print_board(game_board.get_board())

                try:
                    line = input("Chose a line on the board: ")
                    column = input("Chose a column on the board: ")

                    line = line.strip()
                    column = column.strip()

                    if not Check_if_is_an_integer(line) or not Check_if_is_an_integer(column):
                        raise ValueError

                    try:
                        player.place(int(line), int(column))
                    except BoardExceptions as Respective_exception:
                        The_game_ending_exception_message = "Game over !"

                        if Respective_exception.__str__() == The_game_ending_exception_message:
                            self.Print_board(game_board.get_board())
                            print(Respective_exception)
                            print("You win \U0001f600")
                            break

                        print("")
                        print(Respective_exception)
                        print("")

                        player_turn = not player_turn

                except ValueError:
                    print("")
                    print("The chosen line and column need to be integers")
                    print("")
                    player_turn = not player_turn

            else:
                try:
                    robot.execute_a_new_placement()
                except GameHasEndedException as end_message:
                    self.Print_board(game_board.get_board())

                    print(end_message)
                    print("You lost \U0001F923")
                    break

            player_turn = not player_turn


if __name__ == "__main__":
    UI().Start()
