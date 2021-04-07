# Modules
import string
from ... import SprintLog

from .args import Argument
from ..executor.wrapper import Command

from ..handler.params import SprintParams

# Main parser class
class Parser(object):

    def __init__(self, text):
        self.text = text

    def parse(self):

        # Initialization
        value = ""
        flags = ["base"]
        args  = []
        index = -1
        pipet = ""

        # Handle whitespace
        for c in self.text:
            if c in string.whitespace:
                c = c[1:]

            else:
                break

        # Handle loop
        for char in self.text:

            # Character meta
            append = True
            index  += 1

            # Handle quotes
            if char == "\"":

                if "quoted" in flags:
                    flags.remove("quoted")

                else:
                    flags.append("quoted")

                append = False

            # Handle pipes
            if char in [">", "<"] and "quoted" not in flags:

                # Check for invalid continuation
                if pipet and pipet != char:
                    return SprintLog("PipeError", "Pipe ends with unexpected continuation character.")

                # Check for a finished pipe
                if "semi-pipe" in flags:

                    if pipet and pipet == char:
                        flags.remove("semi-pipe")
                        flags.append("has-pipe")

                        pipet = ""

                    elif not pipet:
                        flags.remove("semi-pipe")
                        flags.append("has-pipe")

                # Check for an already existing pipe
                elif "has-pipe" in flags:
                    return SprintLog("PipeError", "No more than 1 pipe permitted.")

                # Create a semi-pipe
                else:
                    flags.append("semi-pipe")
                    pipet = char

            elif "semi-pipe" in flags:
                flags.remove("semi-pipe")  # Prevent characters between a pipe

            # Handle spaces
            if char == " " and "quoted" not in flags or index == len(self.text) - 1:

                # Handle last character
                if index == len(self.text) - 1 and char != "\"":
                    value += char

                # Handle arguments
                if "base" not in flags:
                    args.append(Argument(value))

                else:
                    args.append(Argument(value, base = True))
                    flags.remove("base")

                value = ""
                continue

            # Handle concatenation
            if append:
                value += char

        # No command
        if not args:
            return

        # Handle empty args
        for a in args:
            if not a.arg or a.arg in string.whitespace:
                args.remove(a.arg)

        # Construct parameters
        params  = SprintParams()

        # Check for piping values
        if "has-pipe" in flags:

            # Calculate pipe
            pipeIndex = 0
            pipeType  = None

            for vl in args:

                if vl.is_pipe():
                    pipeType = vl.arg
                    args.remove(vl)
                    break

                pipeIndex += 1

            # Calculate command
            cmdData = []
            if pipeType == ">>":
                new = args[:pipeIndex]
                for a in new:
                    cmdData.append(a)

                args = args[pipeIndex:]

            elif pipeType == "<<":
                new = args[pipeIndex:]
                for a in new:
                    cmdData.append(a)

                args = args[:-pipeIndex]

            # Execute
            cmd = Command(cmdData[0], SprintParams({"args": cmdData[1:]}))
            params.set("pipe", cmd.execute())

        # Process arguments
        base = args[0]
        args = args[1:]

        # Setup parameters
        params.set("args", args)

        # Execute command
        command = Command(base, params)
        command.execute()
