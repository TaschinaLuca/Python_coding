from src.repository.board import obstruction_board
from src.repository.Button import Button

class GridOfButtons:
    def __init__(self, number_of_lines: int, number_of_columns: int, screen, window_size: tuple):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.__screen = screen
        self.__window_size = window_size
        self.__grid = [[' ' for _ in range(self.__number_of_columns)] for _ in range(self.__number_of_lines)]
        self.__button_matrix = []

    def import_grid(self, new_grid):
        self.__grid = new_grid

    def print(self):
        alignment_from_left = 100
        alignment_from_top = 100
        button_width = button_length = 50
        top_alignment = alignment_from_top
        incrementation_factor = 50

        small_grid = (4, 4)
        medium_grid = (5, 6)
        large_grid = (7, 7)

        if (self.__number_of_lines, self.__number_of_columns) == small_grid:
            increment_value = 30
            alignment_from_left += increment_value

        if (self.__number_of_lines, self.__number_of_columns) == medium_grid:
            decrement_value = 10
            alignment_from_left -= decrement_value

        if (self.__number_of_lines, self.__number_of_columns) == large_grid:
            decrement_value = 30
            alignment_from_left -= decrement_value

        self.__button_matrix = []
        for i in range(self.__number_of_lines):
            left_alignment = alignment_from_left
            array_of_buttons = []

            for j in range(self.__number_of_columns):
                text_color = "Blue"
                new_button = Button(left_alignment, top_alignment, button_width, button_length, self.__grid[i][j], text_color, self.__screen)
                new_button.print()
                array_of_buttons.append(new_button)

                left_alignment += incrementation_factor
            self.__button_matrix.append(array_of_buttons)
            top_alignment += incrementation_factor

    def get_matrix_of_buttons(self):
        return self.__button_matrix