from src.repository.board import *


class PlayerServices:
    def __init__(self, board: obstruction_board):
        self.__board = board

    def place(self, line: int, column: int):
        """
        :param line: line of the placed element
        :param column: column of the placed element
        :return:
        """
        if not self.__board.check_if_position_is_in_board(line, column):
            raise OutOfBoundsException

        if not self.__board.check_if_position_is_unmarked(line, column):
            raise OccupiedPositionError

        player_symbol = 'O'
        null = 0

        self.__board.mark_position(line, column, player_symbol)
        if self.__board.get_remaining_unoccupied_cells() == null:
            raise GameHasEndedException
