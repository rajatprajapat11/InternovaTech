import json
import os

CONFIG_FILE = "config.json"


def load_config():
    """
    Load file category configuration.
    """
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        return {}


def get_category(extension):
    """
    Returns the category of a file based on its extension.
    """

    config = load_config()

    extension = extension.lower()

    for category, extensions in config.items():

        if extension in extensions:
            return category

    return "Others"


def count_files(folder_path):
    """
    Count only files (not folders).
    """

    total = 0

    for root, folders, files in os.walk(folder_path):
        total += len(files)

    return total


def get_file_size(size):

    """
    Convert bytes into KB, MB, GB...
    """

    for unit in ["B", "KB", "MB", "GB", "TB"]:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


def is_valid_folder(folder_path):

    """
    Check whether the folder exists.
    """

    return os.path.exists(folder_path)


def create_folder(path):

    """
    Create a folder if it doesn't exist.
    """

    os.makedirs(path, exist_ok=True)


def get_statistics(folder_path):

    import os

    stats = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Music": 0,
        "Archives": 0,
        "Programs": 0,
        "Others": 0,
        "Total": 0
    }

    if not folder_path:
        return stats

    for root, folders, files in os.walk(folder_path):

        for file in files:

            stats["Total"] += 1

            extension = os.path.splitext(file)[1]

            category = get_category(extension)

            if category in stats:
                stats[category] += 1
            else:
                stats["Others"] += 1

    return stats