import os
import shutil
import json

from utils import get_category
from logger import log, error

HISTORY_FILE = "history.json"


def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def organize(folder_path):

    history = load_history()

    moved = 0

    try:

        for item in os.listdir(folder_path):

            source = os.path.join(folder_path, item)

            if os.path.isdir(source):
                continue

            filename, extension = os.path.splitext(item)

            category = get_category(extension)

            destination_folder = os.path.join(folder_path, category)

            os.makedirs(destination_folder, exist_ok=True)

            destination = os.path.join(destination_folder, item)

            counter = 1

            while os.path.exists(destination):

                destination = os.path.join(
                    destination_folder,
                    f"{filename}_{counter}{extension}"
                )

                counter += 1

            shutil.move(source, destination)

            history.append({
                "source": source,
                "destination": destination
            })

            log(f"Moved : {item} → {category}")

            moved += 1

        save_history(history)

        return moved

    except Exception as e:

        error(str(e))

        return 0