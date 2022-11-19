# The main idea of this program is to arrange/manage the files that enters my computer to a certain folder.
# Why? For "order"

# my_common_files are
# for images = jpg, jpeg, png
# for docs = pdf, docx, ppt
# for music = mp3, wav
# for videos =  mp4, mov

# Accessing files in python
import os as my_computer
from os import rename
from os.path import splitext, join, exists
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import logging
import time
import shutil as move

# directories
my_downloads = "C:/Users/adrian/Downloads"
my_images = "C:/Users/adrian/Desktop/Images"
my_videos = "C:/Users/adrian/Desktop/Videos"
my_documents = "C:/Users/adrian/Desktop/Documents"
my_musics = "C:/Users/adrian/Desktop/Musics"

# Formats
image_formats = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", 
                    ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",".k25", ".bmp", 
                    ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", 
                    ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

video_formats = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

documents_formats = [".doc", ".docx", ".odt",
                    ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

music_formats = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

def create_newname(location, name):
    filename, format =  splitext(name) # separates filename including the format
    counter = 1
    while exists(location, name):
        name = filename + str(f"({counter})") + format
        counter += 1
    return name
    
def move_me(location, files_entry, name):
    if exists(location, name):
        new_name = create_newname(location, name)
        same_name = join(location, name)
        new_file_name = join(location, new_name)
        rename(same_name, new_file_name)
    move(files_entry, my_images)

class EventHandler(LoggingEventHandler):
    def events_on_download(self):
        # scandir method is used to access the directory of a certain path
        with scandir(my_downloads) as my_computer:
            for file_entry in my_computer:
                name = file_entry.name
                self.move_images(self, file_entry, name)
                self.move_videos(self, file_entry, name)
                self.move_music(self, file_entry, name)
                self.move_documents(self, file_entry, name)

    def move_images(self, file_entry, name):
        for img_format in image_formats:
            if name.endswith(img_format):
                move_me(my_images, file_entry, name)
                logging.info(name)

    def move_videos(self, file_entry, name):
        for vid_format in video_formats:
            if name.endswith(vid_format):
                move_me(my_videos, file_entry, name)
                logging.info(name)

    def move_music(self, file_entry, name):
        for msc_format in music_formats:
            if name.endswith(msc_format):
                move_me(my_musics, file_entry, name)
                logging.info(name)

    def move_documents(self, file_entry, name):
        for docu_format in documents_formats:
            if name.endswith(docu_format):
                move_me(my_documents, file_entry, name)
                logging.info(name)

# if statement for the directory to run as a script
if __name__ == "__main__":
    # format for the logging info
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M"
    )
    path = my_downloads  # for the path
    # for any modifications/deletions/creation
    event_handler = EventHandler()
    observer = Observer()    # observe
    observer.schedule(event_handler, path, recursive=True)
    observer.start() # execute the observer
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop() # to not break/exit the program for any keyboard input interruption
    observer.join()
