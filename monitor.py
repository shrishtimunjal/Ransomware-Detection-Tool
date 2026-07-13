from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging
from config import MONITOR_FOLDER, THRESHOLD

event_count = 0

logging.basicConfig(
    filename="ransomware.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Monitor(FileSystemEventHandler):

    def process(self, event, action):
        global event_count

        if event.is_directory:
            return

        event_count += 1

        print(f"[{action}] {event.src_path}")
        logging.info(f"{action}: {event.src_path}")

        if event_count >= THRESHOLD:
            print("WARNING: Possible ransomware activity detected!")
            logging.warning("Possible ransomware activity detected!")
            event_count = 0

    def on_created(self, event):
        self.process(event, "CREATED")

    def on_modified(self, event):
        self.process(event, "MODIFIED")

    def on_deleted(self, event):
        self.process(event, "DELETED")

    def on_moved(self, event):
        self.process(event, "MOVED")


observer = Observer()
observer.schedule(Monitor(), MONITOR_FOLDER, recursive=True)
observer.start()

print("Monitoring Started...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()
