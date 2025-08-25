from src.repository.board import *
from random import randint


class RobotServices:
    def __init__(self, board: obstruction_board, difficulty_level):
        self.__board = board
        self.__difficulty = difficulty_level

    def get_a_new_random_valid_position(self) -> (int, int):
        minimum_element = 0
        maximum_line = self.__board.get_length() - 1
        maximum_column = self.__board.get_length() - 1

        while True:
            line = randint(minimum_element, maximum_line)
            column = randint(minimum_element, maximum_column)

            if self.__board.check_if_position_is_unmarked(line, column):
                return [line, column]

    def Create_backup(self, line, column):
        size = 3
        backup_matrix = [[' ' for _ in range(size)] for _ in range(size)]

        line_before = line - 1
        column_before = column - 1
        line_after = line + 1
        column_after = column + 1

        if self.__board.check_if_position_is_in_board(line_before, column_before):
            backup_matrix[0][0] = self.__board.get_position_symbol(line_before, column_before)[:]

        if self.__board.check_if_position_is_in_board(line_before, column):
            backup_matrix[0][1] = self.__board.get_position_symbol(line_before, column)[:]

        if self.__board.check_if_position_is_in_board(line_before, column_after):
            backup_matrix[0][2] = self.__board.get_position_symbol(line_before, column_after)[:]

        if self.__board.check_if_position_is_in_board(line, column_before):
            backup_matrix[1][0] = self.__board.get_position_symbol(line, column_before)[:]

        backup_matrix[1][1] = self.__board.get_position_symbol(line, column)[:]

        if self.__board.check_if_position_is_in_board(line, column_after):
            backup_matrix[1][2] = self.__board.get_position_symbol(line, column_after)[:]

        if self.__board.check_if_position_is_in_board(line_after, column_before):
            backup_matrix[2][0] = self.__board.get_position_symbol(line_after, column_before)[:]

        if self.__board.check_if_position_is_in_board(line_after, column):
            backup_matrix[2][1] = self.__board.get_position_symbol(line_after, column)[:]

        if self.__board.check_if_position_is_in_board(line_after, column_after):
            backup_matrix[2][2] = self.__board.get_position_symbol(line_after, column_after)[:]

        return backup_matrix

    def Undo_the_modifications_on_the_board(self, line, column, backup_matrix):

        line_before = line - 1
        column_before = column - 1
        line_after = line + 1
        column_after = column + 1

        if self.__board.check_if_position_is_in_board(line_before, column_before):
            self.__board.mark_position(line_before, column_before, backup_matrix[0][0])

        if self.__board.check_if_position_is_in_board(line_before, column):
            self.__board.mark_position(line_before, column, backup_matrix[0][1])

        if self.__board.check_if_position_is_in_board(line_before, column_after):
            self.__board.mark_position(line_before, column_after, backup_matrix[0][2])

        if self.__board.check_if_position_is_in_board(line, column_before):
            self.__board.mark_position(line, column_before, backup_matrix[1][0])

        self.__board.mark_position(line, column, backup_matrix[1][1])

        if self.__board.check_if_position_is_in_board(line, column_after):
            self.__board.mark_position(line, column_after, backup_matrix[1][2])

        if self.__board.check_if_position_is_in_board(line_after, column_before):
            self.__board.mark_position(line_after, column_before, backup_matrix[2][0])

        if self.__board.check_if_position_is_in_board(line_after, column):
            self.__board.mark_position(line_after, column, backup_matrix[2][1])

        if self.__board.check_if_position_is_in_board(line_after, column_after):
            self.__board.mark_position(line_after, column_after, backup_matrix[2][2])

    def Calculate_number_of_win_strategies_for_the_robot(self, start_line: int, start_column: int, robot_turn: bool) -> int:
        """
        :param start_line: the line of the last move
        :param start_column: the column of the last move
        :param robot_turn: True if the robot moves thies time, False otherwise
        :return: number of winning strategies for the robot
        """

        symbol = "t"
        self.__board.mark_position(start_line, start_column, symbol)

        if robot_turn:
            output = 0
        else:
            output = 1000000
        null = 0

        if self.__board.get_number_of_free_cels() == null:
            output = 1
            if robot_turn:
                output = 0

            return output
        else:
            for line in range(self.__board.get_length()):
                for column in range(self.__board.get_width()):
                    if self.__board.check_if_position_is_unmarked(line, column):
                        backup_matrix = self.Create_backup(line, column)

                        if robot_turn:
                            output += self.Calculate_number_of_win_strategies_for_the_robot(line, column, not robot_turn)

                            if output >= 50:
                                self.Undo_the_modifications_on_the_board(line, column, backup_matrix)
                                return output
                        else:
                            output = min(output, self.Calculate_number_of_win_strategies_for_the_robot(line, column, not robot_turn))
                            if output == null:
                                self.Undo_the_modifications_on_the_board(line, column, backup_matrix)
                                return output

                        self.Undo_the_modifications_on_the_board(line, column, backup_matrix)
        return output

    def get_a_new_calculated_valid_position(self) -> tuple:
        """
        :return: the optimum position inh the grid
        """
        output_line = 0
        output_column = 0
        the_maximum_number_of_possible_win_strategies = 0

        for line in range(self.__board.get_length()):
            for column in range(self.__board.get_width()):
                if self.__board.check_if_position_is_unmarked(line, column):
                    robot_turn = False
                    backup_matrix = self.Create_backup(line, column)
                    number_of_possible_win_strategies = self.Calculate_number_of_win_strategies_for_the_robot(line, column, robot_turn)
                    self.Undo_the_modifications_on_the_board(line, column, backup_matrix)

                    if number_of_possible_win_strategies >= the_maximum_number_of_possible_win_strategies:
                        the_maximum_number_of_possible_win_strategies = number_of_possible_win_strategies
                        output_line = line
                        output_column = column

        return (output_line, output_column)

    def execute_a_new_placement(self):
        easy = 1
        to_many_free_cells_for_computing_an_optimal_position = 22

        if self.__difficulty == easy or self.__board.get_number_of_free_cels() >= to_many_free_cells_for_computing_an_optimal_position:
            new_position = self.get_a_new_random_valid_position()
        else:
            new_position = self.get_a_new_calculated_valid_position()

        line_index = 0
        column_index = 1
        robot_symbol = 'X'
        null = 0

        self.__board.mark_position(new_position[line_index], new_position[column_index], robot_symbol)
        if self.__board.get_remaining_unoccupied_cells() == null:
            raise GameHasEndedException
