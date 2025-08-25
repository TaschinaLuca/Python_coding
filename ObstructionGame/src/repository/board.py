class obstruction_board:
    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width
        self.__board = [[' ' for _ in range(self.__width)] for _ in range(self.__length)]
        self.__free_cells = length * width

    def get_board(self):
        return self.__board

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_remaining_unoccupied_cells(self):
        return self.__free_cells

    def check_if_position_is_in_board(self, line, column):
        lower_bound = 0

        if line < lower_bound or column < lower_bound or line >= self.__length or column >= self.__width:
            return False

        return True

    def check_if_position_is_unmarked(self, line, column):
        unmarked_element = ' '

        if self.__board[line][column] != unmarked_element:
            return False

        return True

    def get_number_of_free_cels(self):
        return self.__free_cells

    def get_position_symbol(self, line, column) -> str:
        return self.__board[line][column]

    def mark_position(self, line, column, symbol):
        impossible_placement = '*'
        empty_cell = ' '

        if self.check_if_position_is_in_board(line, column) and (self.check_if_position_is_unmarked(line, column) or symbol == empty_cell):
            self.__board[line][column] = symbol

            get_rid_of_the_free_cell = -1
            if self.__board[line][column] == empty_cell:
                self.__free_cells -= get_rid_of_the_free_cell
            else:
                self.__free_cells += get_rid_of_the_free_cell

            if symbol != impossible_placement and symbol != empty_cell:
                line_before = line - 1
                line_after = line + 1
                column_before = column - 1
                column_after = column + 1

                self.mark_position(line_before, column_before, impossible_placement)
                self.mark_position(line_before, column, impossible_placement)
                self.mark_position(line, column_before, impossible_placement)
                self.mark_position(line_before, column_after, impossible_placement)
                self.mark_position(line, column_after, impossible_placement)
                self.mark_position(line_after, column, impossible_placement)
                self.mark_position(line_after, column_after, impossible_placement)
                self.mark_position(line_after, column_before, impossible_placement)


class BoardExceptions(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


class OutOfBoundsException(BoardExceptions):
    def __init__(self):
        super().__init__("Position out of bounds !")


class OccupiedPositionError(BoardExceptions):
    def __init__(self):
        super().__init__("You cannot place anything in this position !")


class GameHasEndedException(BoardExceptions):
    def __init__(self):
        super().__init__("Game over !")
