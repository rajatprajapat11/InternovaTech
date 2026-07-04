import os
import json
import shutil

from logger import log, error

HISTORY_FILE = "history.json"


def undo_last_operation():
    """
    Restore all files moved during the last organization.
    """

    try:

        if not os.path.exists(HISTORY_FILE):
            return 0

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)

        if len(history) == 0:
            return 0

        restored = 0

        # Restore files in reverse order
        for item in reversed(history):

            source = item["destination"]
            destination = item["source"]

            if os.path.exists(source):

                os.makedirs(os.path.dirname(destination), exist_ok=True)

                shutil.move(source, destination)

                restored += 1

                log(f"Undo : {source} -> {destination}")

        # Clear history after undo
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

        return restored

    except Exception as e:

        error(str(e))

        return 0