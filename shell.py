# Copyright 2021; iiPython

# Modules
from sprint import Parser, console

# Command grabber
def command_input(indent = 0):

    # Handle input
    text = console.input("[green]Sprint [yellow]>> [/yellow]" + (" " * indent))

    # Check for backslashes
    if text.endswith("\\"):
        text = text[:-1] + command_input(indent + 2)

    # Return our command
    return text

# Main shell loop
while True:
    try:
        command = command_input()

    except KeyboardInterrupt:
        print("^C")
        continue

    # Load parser
    parser = Parser(command)
    parser.parse()
