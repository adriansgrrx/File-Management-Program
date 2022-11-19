# The main idea of this program is to arrange/manage the files that enters my computer to a certain folder.
# Why? For "order"

# Accessing files in python
import os as my_computer
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import logging
import time

my_downloads = "C:/Users/adrian/Downloads"
# scandir method is used to access the directory of a certain path
for files in my_computer.scandir(my_downloads):
    print(files.name)
    

# if statement for the directory to run as a script 
if __name__ == "__main__":
    # format for the logging info
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s -%(message)s",
        datefmt="%Y-%m-%d %H:%M"
    )
    # for the path
    path = my_downloads
    # for any modifications/deletions/creation
    event_handler = LoggingEventHandler()
    # observe
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    # execute the observer
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop() # to break/exit the program for any keyboard input interruption
    observer.join()
