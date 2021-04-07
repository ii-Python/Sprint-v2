# loader.py
# handles command loading

# Modules
import os
import json
from ..handler.logging import Logger
from os.path import isdir, isfile, join

# Main loader class
class Loader(object):
    def __init__(self, path: list = []):
        self.path = path
        self.logger = Logger()

        if not self.path:
            self.logger.warn("sprint path is empty, no commands will be loaded.")

    def locate_command(self, name: str):

        # Convert argument to string
        name = repr(name)

        # Loop through path
        MATCHING = []
        for PATH_DIR in self.path:
            if not isdir(PATH_DIR):
                self.logger.warn(f"PATH directory '{PATH_DIR}' does not exist, skipped.")
                continue

            # Loop through publishers
            for PUBLISHER in os.listdir(PATH_DIR):
                PUB_PATH = join(PATH_DIR, PUBLISHER)

                # Handle metadata
                author = ("unknown", "unknown")
                metafile = join(PUB_PATH, "METADATA")

                if isfile(metafile):
                    try:
                        with open(metafile, "r") as file:
                            meta = file.read()

                        meta = json.loads(meta)
                        author = (meta["author"], meta["author_contact"])

                    except json.JSONDecodeError:
                        pass

                # Loop through modules
                for MODULE in os.listdir(PUB_PATH):
                    MOD_PATH = join(PUB_PATH, MODULE)

                    if not isdir(MOD_PATH):
                        continue  # Skip METADATA and asset files (READMEs, etc)

                    # Loop through commands
                    for COMMAND in os.listdir(MOD_PATH):
                        CMD_PATH = join(MOD_PATH, COMMAND)

                        # Check valdiity
                        if not isfile(CMD_PATH):
                            continue  # Skip asset folders

                        # Grab data
                        cmd_name = COMMAND.split("\\")[-1].split(".")[0]

                        # Check name
                        if cmd_name != name:
                            continue

                        # Take note
                        MATCHING.append({
                            "command": {
                                "name": cmd_name,
                                "path": CMD_PATH,
                                "full_name": author[0] + "." + cmd_name
                            },
                            "author": author,
                            "module": {
                                "name": MODULE,
                                "path": MOD_PATH
                            }
                        })

        # Handle conflicts
        STATUS = False
        if len(MATCHING) > 1:
            STATUS = True
            MATCHING = [_["command"]["full_name"] for _ in MATCHING]

        # Return matching commands
        return STATUS, MATCHING
