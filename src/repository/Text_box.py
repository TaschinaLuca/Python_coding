import pygame

pygame.init()
font_size = 24
font = pygame.font.Font(None, font_size)

class TextBox:
    def __init__(self, width: int, length: int, start_x: int, start_y: int, text_color: str, text: str, screen):
        self.__width = width
        self.__length = length
        self.__color = text_color
        self.__text = text
        self.__screen = screen
        self.__start_x = start_x
        self.__start_y = start_y

    def print(self):
        chosen_color = self.__color
        font_size = 24

        font = pygame.font.Font(None, font_size)
        text = font.render(self.__text, True, chosen_color)
        rectangle_surface = pygame.Surface((self.__width, self.__length))
        text_rectangle = text.get_rect(center=(rectangle_surface.get_width() / 2, rectangle_surface.get_height() / 2))

        rectangle_start_x = 0
        rectangle_start_y = 0
        chosen_rectangle_color = "White"
        pygame.draw.rect(rectangle_surface, chosen_rectangle_color,
                         (rectangle_start_x, rectangle_start_y, self.__width, self.__length))

        rectangle_start_x = self.__start_x
        rectangle_start_y = self.__start_y
        rectangle_surface.blit(text, text_rectangle)
        button_rect = pygame.Rect(rectangle_start_x, rectangle_start_y, self.__width,
                                  self.__length)  # Adjust the position as needed

        # Draw the button on the screen
        self.__screen.blit(rectangle_surface, (button_rect.x, button_rect.y))
