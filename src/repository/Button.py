import pygame

pygame.init()
font_size = 24
font = pygame.font.Font(None, font_size)

class Button:

    def __init__(self, starting_x: int, starting_y: int, width: int, length: int, text: str, text_color: str, screen):
        self.__start_x = starting_x
        self.__width = width
        self.__start_y = starting_y
        self.__length = length
        self.__text = font.render(text, True, text_color)
        self.__screen = screen

    def print(self):
        button_surface = pygame.Surface((self.__width, self.__length))
        text_rect = self.__text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))

        rectangle_start_x = 0
        rectangle_start_y = 0
        button_color = "White"

        pygame.draw.rect(button_surface, button_color, (rectangle_start_x, rectangle_start_y, self.__width, self.__length))
        if self.get_rectangle.collidepoint(pygame.mouse.get_pos()):
            new_button_color = (127, 255, 212)
            rectangle_start_x = 10
            rectangle_start_y = 10
            decrementing_value = 20

            rectangle_width = self.__width - decrementing_value
            rectangle_length = self.__length - decrementing_value

            pygame.draw.rect(button_surface, new_button_color, (rectangle_start_x, rectangle_start_y, rectangle_width, rectangle_length))

        button_surface.blit(self.__text, text_rect)
        button_rect = pygame.Rect(self.__start_x, self.__start_y, self.__width, self.__length)  # Adjust the position as needed

        # Draw the button on the screen
        self.__screen.blit(button_surface, (button_rect.x, button_rect.y))

    @property
    def get_rectangle(self):
        return pygame.Rect(self.__start_x, self.__start_y, self.__width, self.__length)
