from src.ui.GUI_ui import *
from src.ui.Console_ui import *

if __name__ == "__main__":
    input_file = open('execution_mode', 'r')
    text = input_file.read()

    Play_in_GUI = "GUI"
    Play_in_Console = "Console"

    if text == Play_in_Console:
        UserInterface = UI
        UserInterface().Start()

    elif text == Play_in_GUI:
        UserInterface = GUI
        UserInterface().start_menu()
