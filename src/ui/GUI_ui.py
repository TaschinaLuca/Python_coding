from src.repository.Button import Button
from src.repository.Text_box import TextBox
from src.repository.Grid_of_buttons import GridOfButtons
from src.services.GUI_services import *
from src.services.robot_services import *
import pygame
import sys


class GUI:
    def start_menu(self):
        pygame.init()
        clock = pygame.time.Clock()
        clock.tick(30)

        window_size = (500, 600)
        screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
        button_width = 150
        button_length = 50
        alignment_from_left = 150

        alignment_from_top = 100
        start_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "Start", "Blue", screen)
        alignment_from_top = 150
        quit_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "Quit", "Blue", screen)

        while True:
            image_name = 'apa1.jpg'

            background_image = pygame.image.load(image_name).convert_alpha()

            starting_point = (0, 0)
            screen.blit(background_image, starting_point)

            main_menu_caption = 'Main Menu'
            pygame.display.set_caption(main_menu_caption)

            for event in pygame.event.get():
                # Check for the quit event
                if event.type == pygame.QUIT:
                    # Quit the game
                    pygame.quit()
                    sys.exit()

                # Check for the mouse button down event

                one_event = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == one_event:
                    if start_button.get_rectangle.collidepoint(event.pos):
                        self.difficulty_select_menu()

                    if quit_button.get_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.VIDEORESIZE:
                        screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            quit_button.print()
            start_button.print()

            # Update the game state
            pygame.display.update()

    def difficulty_select_menu(self):
        pygame.init()

        clock = pygame.time.Clock()
        clock.tick(30)

        # Create a Pygame window
        window_size = (500, 600)
        screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
        button_width = 150
        button_length = 50
        alignment_from_left = 150

        alignment_from_top = 100
        easy_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "Easy", "Blue", screen)
        alignment_from_top = 150
        hard_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "Hard", "Blue", screen)
        alignment_from_top = 500
        back_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "Back", "Blue", screen)

        while True:
            image_name = 'Water.jpg'
            background_image = pygame.image.load(image_name).convert_alpha()

            starting_point = (0, 0)
            screen.blit(background_image, starting_point)
            pygame.display.set_caption('Difficulty select menu')

            width_of_text_rectangle = 150
            length_of_text_rectangle = 50
            chosen_color = "Blue"
            text_to_be_shown = "Chose difficulty"

            start_x = 150
            start_y = 50
            Text_to_be_shown = TextBox(width_of_text_rectangle, length_of_text_rectangle, start_x, start_y, chosen_color, text_to_be_shown, screen)

            for event in pygame.event.get():
                # Check for the quit event
                if event.type == pygame.QUIT:
                    # Quit the game
                    pygame.quit()
                    sys.exit()

                # Check for the mouse button down event
                one_event = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == one_event:
                    if easy_button.get_rectangle.collidepoint(event.pos):
                        difficulty_level = 1
                        self.select_size_nemu(difficulty_level)

                    if hard_button.get_rectangle.collidepoint(event.pos):
                        difficulty_level = 2
                        self.select_size_nemu(difficulty_level)

                    if back_button.get_rectangle.collidepoint(event.pos):
                        return

                    if event.type == pygame.VIDEORESIZE:
                        screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            easy_button.print()
            hard_button.print()
            back_button.print()
            Text_to_be_shown.print()

            # Update the game state
            pygame.display.update()

    def select_size_nemu(self, difficulty_level):
        pygame.init()

        clock = pygame.time.Clock()
        clock.tick(30)

        # Create a Pygame window
        window_size = (500, 600)
        screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
        button_width = 150
        button_length = 50
        alignment_from_left = 150

        alignment_from_top = 500
        back_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "Back", "Blue", screen)
        alignment_from_top = 100
        small_size_grid_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "small", "Blue", screen)
        alignment_from_top = 150
        medium_size_grid_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "medium", "Blue", screen)
        alignment_from_top = 200
        large_size_grid_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "large", "Blue", screen)

        width_of_text_rectangle = 150
        length_of_text_rectangle = 50
        chosen_color = "Blue"
        text_to_be_shown = "Chose grid size"
        start_x = 150
        start_y = 50

        Text_to_be_shown = TextBox(width_of_text_rectangle, length_of_text_rectangle, start_x, start_y, chosen_color, text_to_be_shown, screen)

        while True:
            image_name = 'apa3.jpg'
            background_image = pygame.image.load(image_name).convert_alpha()

            starting_point = (0, 0)
            screen.blit(background_image, starting_point)

            game_menu_caption = 'Game on '

            easy = 1
            hard = 2
            if difficulty_level == easy:
                game_menu_caption = game_menu_caption + 'easy difficulty'
            elif difficulty_level == hard:
                game_menu_caption = game_menu_caption + 'hard difficulty'
            pygame.display.set_caption(game_menu_caption)

            for event in pygame.event.get():
                # Check for the quit event
                if event.type == pygame.QUIT:
                    # Quit the game
                    pygame.quit()
                    sys.exit()

                one_event = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == one_event:
                    if back_button.get_rectangle.collidepoint(event.pos):
                        return

                    if event.type == pygame.VIDEORESIZE:
                        screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                    if small_size_grid_button.get_rectangle.collidepoint(event.pos):
                        number_of_lines = 4
                        number_of_columns = 4
                        self.run_game(number_of_lines, number_of_columns, difficulty_level)

                    if medium_size_grid_button.get_rectangle.collidepoint(event.pos):
                        number_of_lines = 5
                        number_of_columns = 6
                        self.run_game(number_of_lines, number_of_columns, difficulty_level)

                    if large_size_grid_button.get_rectangle.collidepoint(event.pos):
                        number_of_lines = 7
                        number_of_columns = 7
                        self.run_game(number_of_lines, number_of_columns, difficulty_level)

            small_size_grid_button.print()
            medium_size_grid_button.print()
            large_size_grid_button.print()
            back_button.print()
            Text_to_be_shown.print()
            pygame.display.update()

    def run_game(self, number_of_lines_in_the_grid, number_of_column_in_the_grid, difficulty_level):
        pygame.init()

        clock = pygame.time.Clock()
        clock.tick(30)

        # Create a Pygame window
        window_size = (500, 600)
        screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
        button_width = 150
        button_length = 50
        alignment_from_left = 150
        alignment_from_top = 500
        back_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "Back", "Blue", screen)
        ##############
        alignment_from_left = 155
        alignment_from_top = 50
        hint_button = Button(alignment_from_left, alignment_from_top, button_width, button_length, "Hint", "Blue", screen)
        ##############

        player_turn = True
        grid = GridOfButtons(number_of_lines_in_the_grid, number_of_column_in_the_grid, screen, window_size)
        associated_board = obstruction_board(number_of_lines_in_the_grid, number_of_column_in_the_grid)
        robot = RobotServices(associated_board, difficulty_level)
        GUI_service = GUI_services()
        You_won = False
        You_lost = False

        while True:
            grid.import_grid(associated_board.get_board())
            grid.print()

            image_name = 'Water.jpg'
            background_image = pygame.image.load(image_name).convert_alpha()

            starting_point = (0, 0)
            screen.blit(background_image, starting_point)

            game_menu_caption = 'Game on '

            easy = 1
            hard = 2
            if difficulty_level == easy:
                game_menu_caption = game_menu_caption + 'easy difficulty'
            elif difficulty_level == hard:
                game_menu_caption = game_menu_caption + 'hard difficulty'
            pygame.display.set_caption(game_menu_caption)

            if not player_turn and not You_lost and not You_won:
                try:
                    robot.execute_a_new_placement()
                    player_turn = not player_turn
                except GameHasEndedException:
                    You_lost = True

            for event in pygame.event.get():
                # Check for the quit event
                if event.type == pygame.QUIT:
                    # Quit the game
                    pygame.quit()
                    sys.exit()

                one_event = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == one_event:
                    if back_button.get_rectangle.collidepoint(event.pos):
                        return

                    elif event.type == pygame.VIDEORESIZE:
                        screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
####################
                    if hint_button.get_rectangle.collidepoint(event.pos) and not You_won and not You_lost and player_turn:
                        try:
                            to_many_free_cells_for_computing_an_optimal_position = 22
                            if associated_board.get_number_of_free_cels() <= to_many_free_cells_for_computing_an_optimal_position:
                                hint_position = robot.get_a_new_calculated_valid_position()
                            else:
                                hint_position = robot.get_a_new_random_valid_position()

                            player_turn = not player_turn
                            line = 0
                            column = 1
                            player_symbol = "O"
                            associated_board.mark_position(hint_position[line], hint_position[column], player_symbol)

                            null = 0
                            if associated_board.get_number_of_free_cels() == null:
                                raise GameHasEndedException

                        except GameHasEndedException:
                            if not player_turn:
                                You_won = True
                            else:
                                You_lost = True
####################
                    elif not You_lost and not You_won:
                        try:
                            the_grid_has_changed = GUI_service.Verify_where_the_player_clicked_and_mark_that_cell(grid.get_matrix_of_buttons(), associated_board, event)
                            if the_grid_has_changed:
                                player_turn = not player_turn
                        except GameHasEndedException:
                            You_won = True

            if You_won:
                width_of_text_rectangle = 150
                length_of_text_rectangle = 50
                chosen_color = "Blue"
                text_to_be_shown = "You win"
                start_x = 155
                start_y = 50

                Text_to_be_shown = TextBox(width_of_text_rectangle, length_of_text_rectangle, start_x, start_y,
                                           chosen_color, text_to_be_shown, screen)
                Text_to_be_shown.print()

            if You_lost:
                width_of_text_rectangle = 150
                length_of_text_rectangle = 50
                chosen_color = "Blue"
                text_to_be_shown = "You lost"
                start_x = 155
                start_y = 50

                Text_to_be_shown = TextBox(width_of_text_rectangle, length_of_text_rectangle, start_x, start_y, chosen_color, text_to_be_shown, screen)
                Text_to_be_shown.print()

            ######
            if not You_won and not You_lost:
                hint_button.print()
            ######

            grid.import_grid(associated_board.get_board())
            grid.print()
            back_button.print()
            pygame.display.update()

if __name__ == "__main__":
    UserInterface = GUI
    UserInterface().start_menu()

