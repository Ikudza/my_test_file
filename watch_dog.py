# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    
    def on_any_event(self, event):
        print('Fire!')
        #os.system('manage.py collectstatic')

        
if __name__ == '__main__':

    observer = Observer()
    observer.schedule(
        Handler(), path=os.path.dirname(__file__), recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
