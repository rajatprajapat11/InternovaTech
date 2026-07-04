from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

from organizer import organize


class FolderWatcher(FileSystemEventHandler):

    def __init__(self, folder):
        self.folder = folder

    def on_created(self, event):

        if event.is_directory:
            return

        print(f"\nNew File Detected : {event.src_path}")

        organize(self.folder)


def start_monitoring(folder):

    event_handler = FolderWatcher(folder)

    observer = Observer()

    observer.schedule(event_handler, folder, recursive=False)

    observer.start()

    print("\nMonitoring Started...")
    print("Press CTRL + C to Stop.\n")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()