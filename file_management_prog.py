# The main idea of this program is to arrange/manage the files that enters my computer to a certain folder.
# Why? For "order"

# my_common_files are
# for images = jpg, jpeg, png
# for docs = pdf, docx, ppt
# for music = mp3, wav
# for videos =  mp4, mov

# Accessing files in python
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import time

# directories
my_downloads = "C:/Users/adrian/Downloads"
# folders
my_images = "C:/Users/adrian/Desktop/Images"
my_videos = "C:/Users/adrian/Desktop/Videos"
my_documents = "C:/Users/adrian/Desktop/Documents"
my_musics = "C:/Users/adrian/Desktop/Musics"

# Formats
image_formats = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", 
                    ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",".k25", ".bmp", 
                    ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", 
                    ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

video_formats = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

documents_formats = [".doc", ".docx", ".odt",
                    ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

music_formats = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

def create_newname(location, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{location}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_me(location, file_entry, name):
    if exists(f"{location}/{name}"):
        new_name = create_newname(location, name)
        same_name = join(location, name)
        new_file_name = join(location, new_name)
        rename(same_name, new_file_name)
    move(file_entry, location)

class EventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(my_downloads) as my_files:
            for files in my_files:
                name = files.name
                self.move_images(files, name)
                self.move_videos(files, name)
                self.move_documents(files, name)
                self.move_musics(files, name)

    def move_images(self, file_entry, name):
        for img_format in image_formats:
            if name.endswith(img_format) or name.endswith(img_format.upper()):
                move_me(my_images, file_entry, name)
                logging.info(f"Moved image file: {name}")

    def move_videos(self, file_entry, name):
        for vid_format in video_formats:
            if name.endswith(vid_format) or name.endswith(vid_format.upper()):
                move_me(my_videos, file_entry, name)
                logging.info(f"Moved video file: {name}")

    def move_documents(self, file_entry, name):
        for docu_format in documents_formats:
            if name.endswith(docu_format) or name.endswith(docu_format.upper()):
                move_me(my_documents, file_entry, name)
                logging.info(f"Moved document file: {name}")

    def move_musics(self, file_entry, name):
        for msc_format in music_formats:
            if name.endswith(msc_format) or name.endswith(msc_format.upper()):
                move_me(my_musics, file_entry, name)
                logging.info(f"Moved audio file: {name}")

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
