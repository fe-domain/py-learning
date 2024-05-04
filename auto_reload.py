
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alien_invasion import run_game


class MyHandler(FileSystemEventHandler):
    def __init__(self, filename, callback):
        super().__init__()
        self.filename = filename
        self.callback = callback

    def on_modified(self, event):
        if event.src_path.endswith(self.filename):
            self.callback()


def run_code():
    # 在这里编写需要运行的代码
    run_game()


if __name__ == "__main__":
    filename = "your_script.py"  # 替换为你的 Python 文件名
    event_handler = MyHandler(filename, run_code)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
