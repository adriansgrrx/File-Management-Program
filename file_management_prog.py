# The main idea of this program is to arrange/manage the files that enters my computer to a certain folder.
# Why? For "order"

# my_common_files are
# for images = jpg, jpeg, png
# for docs = pdf, docx, ppt
# for music = mp3, wav
# for videos =  mp4, mov

# Accessing files in python
import os as my_computer
from os.path import splitext, join, exists
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import logging
import time
import shutil as move

my_downloads = "C:/Users/adrian/Downloads"
my_images = "C:/Users/adrian/Desktop/Images"

def create_newname(location, name):
    filename, format =  splitext(name) # separates filename including the format
    counter = 1
    while exists(location, name):
        name = filename + str(f"({counter})") + format
        counter += 1
    return name
    
def move_me(location, files_entry, name):
    move(files_entry, my_images)



class EventHandler(LoggingEventHandler):
    def events_on_download(self):
        # scandir method is used to access the directory of a certain path
        for file_entry in my_computer.scandir(my_downloads):
            name = file_entry.name
            self.move_images(self, file_entry, name)

    def move_images(self, file_entry, name):
        if name.endswith("jpg"):
            move_me(my_images, file_entry, name)
            logging.info(name)

        
        






# if statement for the directory to run as a script
if __name__ == "__main__":
    # format for the logging info
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctEventHandlerime)s -%(message)s",
        datefmt="%Y-%m-%d %H:%M"
    )
    # for the path
    path = my_downloads
    # for any modifications/deletions/creation
    event_handler = EventHandler()
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
