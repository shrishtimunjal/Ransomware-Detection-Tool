import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folder to monitor (change this to your folder path)
MONITOR_FOLDER = "D:\\CyberSecurity\\TestFolder"

# Logging configuration
logging.basicConfig(
    filename="ransomware.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

event_counter = 0
THRESHOLD = 10


class RansomwareDetector(FileSystemEventHandler):

    def process_event(self, event_type, event):
        global event_counter

        if event.is_directory:
            return

        event_counter += 1

        print(f"[{event_type}] {event.src_path}")
        logging.info(f"{event_type}: {event.src_path}")

        if event_counter >= THRESHOLD:
            print("\n⚠ WARNING: Possible ransomware activity detected!")
            logging.warning("Possible ransomware activity detected!")
            event_counter = 0

    def on_created(self, event):
        self.process_event("CREATED", event)

    def on_modified(self, event):
        self.process_event("MODIFIED", event)

    def on_deleted(self, event):
        self.process_event("DELETED", event)

    def on_moved(self, event):
        self.process_event("MOVED", event)


if __name__ == "__main__":

    event_handler = RansomwareDetector()
    observer = Observer()
    observer.schedule(event_handler, MONITOR_FOLDER, recursive=True)

    observer.start()

    print("=" * 50)
    print("RANSOMWARE DETECTION TOOL")
    print("Monitoring Folder:", MONITOR_FOLDER)
    print("=" * 50)

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
