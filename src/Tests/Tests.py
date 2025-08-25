from src.repository.board import obstruction_board
from src.repository.Button import Button
from src.repository.Grid_of_buttons import GridOfButtons
from src.repository.Text_box import TextBox
from src.services.player_services import *
from src.services.robot_services import *
from src.services.some_functions import *
from src.services.GUI_services import GUI_services
import unittest

class Test(unittest.TestCase):

    def test_exceptions(self):

        try:
            raise OutOfBoundsException
        except OutOfBoundsException:
            pass

        try:
            raise OccupiedPositionError
        except OccupiedPositionError:
            pass

        try:
            raise GameHasEndedException
        except GameHasEndedException:
            pass

    def test_repositories(self):
        game_board = obstruction_board(1, 1)
        self.assertEquals(game_board.get_board(), [[' ']])
        self.assertEquals(game_board.check_if_position_is_unmarked(0, 0), True)

        game_board.mark_position(0, 0, 'X')
        self.assertEquals(game_board.check_if_position_is_unmarked(0, 0), False)
        self.assertEquals(game_board.check_if_position_is_in_board(1, 0), False)
        self.assertEquals(game_board.check_if_position_is_in_board(0, 0), True)
        self.assertEquals(game_board.get_number_of_free_cels(), 0)
        self.assertEquals(game_board.get_width(), 1)
        self.assertEquals(game_board.get_length(), 1)

        game_board.mark_position(0, 0, ' ')
        self.assertEquals(game_board.get_position_symbol(0, 0), ' ')

    def test_services(self):
        self.assertEquals(Check_if_is_an_integer("123"), True)
        self.assertEquals(Check_if_is_an_integer("ana"), False)

        game_board = obstruction_board(5, 5)
        player = PlayerServices(game_board)
        robot = RobotServices(game_board, 1)

        player.place(0, 0)
        self.assertEquals(game_board.check_if_position_is_unmarked(0, 0), False)
        self.assertEquals(game_board.check_if_position_is_unmarked(4, 4), True)

        position = robot.get_a_new_random_valid_position()
        self.assertEquals(game_board.check_if_position_is_unmarked(position[0], position[1]), True)

        position = robot.get_a_new_calculated_valid_position()
        self.assertEquals(game_board.check_if_position_is_unmarked(position[0], position[1]), True)


if __name__ == "__main__":
    Tests = Test()

    Tests.test_exceptions()
    Tests.test_repositories()
    Tests.test_services()

# python -m coverage run -m unittest discover src/Tests
# python -m coverage report