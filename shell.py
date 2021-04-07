# Copyright 2021; iiPython

# Modules
from sprint import Parser, colored

# Command grabber
def command_input(indent = 0):

    # Handle input
    text = input(colored("Sprint >> " + (" " * indent), "green"))

    # Check for backslashes
    if text.endswith("\\"):
        text = text[:-1] + command_input(indent + 2)

    # Return our command
    return text

# Main shell loop
while True:
    command = command_input()

    # Load parser
    parser = Parser(command)
    parser.parse()
