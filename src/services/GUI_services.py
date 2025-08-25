from src.repository.board import obstruction_board
from src.services.player_services import PlayerServices
import pygame

pygame.init()

class GUI_services:
    def Verify_where_the_player_clicked_and_mark_that_cell(self, matrix_of_buttons: list, game_board: obstruction_board, new_event) -> bool:
        player_service = PlayerServices(game_board)

        for line in range(len(matrix_of_buttons)):
            for column in range(len(matrix_of_buttons[line])):
                if matrix_of_buttons[line][column].get_rectangle.collidepoint(new_event.pos) and game_board.check_if_position_is_unmarked(line, column):
                    player_service.place(line, column)
                    return True

        return False
