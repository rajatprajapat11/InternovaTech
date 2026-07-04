from datetime import datetime

LOG_FILE = "activity.log"


def log(message):
    """
    Write a normal log message.
    """

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[INFO] {current_time} : {message}\n")


def warning(message):
    """
    Write a warning message.
    """

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[WARNING] {current_time} : {message}\n")


def error(message):
    """
    Write an error message.
    """

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[ERROR] {current_time} : {message}\n")