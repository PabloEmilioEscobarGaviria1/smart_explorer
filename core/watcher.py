from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FolderHandler(FileSystemEventHandler):

    def __init__(self, callback):
        self.callback = callback

    def on_any_event(self, event):
        self.callback()


class FolderWatcher:

    def __init__(self, path, callback):

        self.observer = Observer()
        handler = FolderHandler(callback)

        self.observer.schedule(handler, path, recursive=False)

    def start(self):
        self.observer.start()

    def stop(self):
        self.observer.stop()