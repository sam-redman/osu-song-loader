# ---------------------------------- MODULES ---------------------------------- #

import os
import glob
import time
import tkinter.filedialog
from tkinter import *

# ---------------------------------- MAIN ---------------------------------- #


def load():
    """Load .osz files in the directory with a 2 second delay between each file load."""

    # Grab the entry in the directory entry box.
    directory = directory_entry.get()
    # Loop through the directory and open each file. Wait two seconds between each file.
    for filepath in glob.glob(os.path.join(directory, '*.osz')):
        os.startfile(filepath)
        time.sleep(2)


def chose_directory():
    """Let the user pick the folder that the .osz file are saved in."""

    # Opens a dialog box to allow for easy navigation to the file directory.
    chosen_directory = tkinter.filedialog.askdirectory()
    # Insert the chosen directory in text format in the entry box.
    directory_entry.insert(0, chosen_directory)

# ---------------------------- UI SETUP ------------------------------- #


# Create window.
window = Tk()
window.title("osu! Song Loader")
# Padding, background colour.
window.config(padx=50, pady=50, bg="#ff66aa")

# Directory.
directory_button = Button(width=11, text="Song Directory", command=chose_directory)
directory_button.grid(column=1, row=1)

directory_entry = Entry(width=40)
directory_entry.grid(column=2, row=1, padx=5)

# Loader.
load_song_button = Button(width=11, text="Load", command=load)
load_song_button.grid(column=1, row=2, pady=5)

# ---------------------------- RUN ------------------------------- #

# Keeps window on screen.
window.mainloop()
