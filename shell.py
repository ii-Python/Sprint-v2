# Modules
from sprint import Parser

# Main loop
while True:
    x = input("> ")

    p = Parser(x)
    p.parse()
